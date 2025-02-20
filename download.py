from datetime import datetime, timedelta
import os
from alpaca.data import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import pandas as pd

# Manually read .env file
with open('.env') as f:
    for line in f:
        key, value = line.strip().split('=')
        os.environ[key] = value

# Load environment variables
load_dotenv()

# Initialize client with API keys
client = CryptoHistoricalDataClient(
    api_key=os.getenv('ALPACA_API_KEY'),
    secret_key=os.getenv('ALPACA_SECRET_KEY')
)

# Define parameters
symbols = ['BTC/USD', 'ETH/USD']  # Add more symbols as needed
end_date = datetime.now()
start_date = end_date - timedelta(days=30)  # Last 30 days

# Request parameters
request_params = CryptoBarsRequest(
    symbol_or_symbols=symbols,
    timeframe=TimeFrame.Minute,
    start=start_date,
    end=end_date
)

# Get the data
bars = client.get_crypto_bars(request_params)

# Convert to pandas DataFrame
df = bars.df

# Reset index to make timestamp a column
df = df.reset_index()

# Save to CSV
output_file = 'crypto_data_1min.csv'
df.to_csv(output_file, index=False)
print(f"Data downloaded and saved to {output_file}")
print(f"Data shape: {df.shape}")
print("\nFirst few rows of data:")
print(df.head())
