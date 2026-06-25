stock_prices = {
    "AAPL": 150,
    "TSLA": 250,
    "GOOGLE": 2800,
    "AMAZON": 3300
}

total = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or done): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        total += stock_prices[stock] * qty
    else:
        print("Stock not found!")

print("Total Investment Value:", total)