product_prices = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
    "date": 4
}

if __name__ == '__main__':
    print(product_prices["apple"])
    print(product_prices.get("grape", "Not Found"))