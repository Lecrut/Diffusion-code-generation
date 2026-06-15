def calculate_total_cost(prices):
    total = 0
    for price in prices.values():
        total += price
    return total
if __name__ == '__main__':
    product_prices = {
        "apple": 1.50,
        "banana": 0.75,
        "orange": 1.25,
        "grape": 3.00
    }
    total_cost = calculate_total_cost(product_prices)
    print(total_cost)