import locale
import requests
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

global_url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

request = requests.get(url=global_url, headers={'X-CMC_PRO_API_KEY': 'Your_API_Key'})
result = request.json()
data = result['data']
global_cap = round(data['stablecoin_market_cap'], 2)

table = PrettyTable([
    'Name',
    'Ticker',
    '% of total global cap',
    'Current',
    '$10.9T (Gold)',
    '$35.2T (Narrow Money)',
    '$89.5T (World Stock Market)',
    '$95.7T (Broad Money)',
    '$280.6T (Real Estate)',
    '$570.1T (Derivatives)'
])

request = requests.get(url=ticker_url, headers={'X-CMC_PRO_API_KEY': 'Your_API_Key'})
result = request.json()
data = result['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    percentage_of_global_cap = float(currency['quote']['USD']['market_cap']) / float(global_cap)

    current_price = round(float(currency['quote']['USD']['price']), 2)
    available_supply = float(currency['total_supply'])

    if available_supply > 0:
        trillion10price = round(10900000 * percentage_of_global_cap / available_supply, 2)
        trillion35price = round(35200000 * percentage_of_global_cap / available_supply, 2)
        trillion89price = round(89500000 * percentage_of_global_cap / available_supply, 2)
        trillion95price = round(95700000 * percentage_of_global_cap / available_supply, 2)
        trillion280price = round(280600000 * percentage_of_global_cap / available_supply, 2)
        trillion570price = round(570100000 * percentage_of_global_cap / available_supply, 2)
    else:
        trillion10price = 0
        trillion35price = 0
        trillion89price = 0
        trillion95price = 0
        trillion280price = 0
        trillion570price = 0

    percentage_of_global_cap_string = str(round(percentage_of_global_cap * 100, 2)) + '%'
    current_price_string = '$' + str(current_price)
    trillion10price_string = '$' + locale.format_string('%.2f', trillion10price, True)
    trillion35price_string = '$' + locale.format_string('%.2f', trillion35price, True)
    trillion89price_string = '$' + locale.format_string('%.2f', trillion89price, True)
    trillion95price_string = '$' + locale.format_string('%.2f', trillion95price, True)
    trillion280price_string = '$' + locale.format_string('%.2f', trillion280price, True)
    trillion570price_string = '$' + locale.format_string('%.2f', trillion570price, True)

    table.add_row([
        name,
        ticker,
        percentage_of_global_cap_string,
        current_price_string,
        trillion10price_string,
        trillion35price_string,
        trillion89price_string,
        trillion95price_string,
        trillion280price_string,
        trillion570price_string
    ])

print()
print(table)
print()
