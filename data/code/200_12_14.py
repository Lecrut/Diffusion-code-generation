class DataProcessor:
    KEY_NAME = 'name'
    KEY_PRICE = 'price'

    @staticmethod
    def extract_prices(data):
        return list(map(lambda x: x.get(DataProcessor.KEY_PRICE, 0), data))

if __name__ == '__main__':
    product_list = [
        {'name': 'Laptop', 'price': 1200.50, 'quantity': 1},
        {'name': 'Mouse', 'price': 25.99, 'quantity': 2},
        {'name': 'Keyboard', 'price': 75.00, 'quantity': 1},
        {'name': 'Monitor', 'price': 350.75, 'quantity': 1}
    ]
    processor = DataProcessor()
    prices = processor.extract_prices(product_list)
    print(prices)