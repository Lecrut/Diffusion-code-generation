class DictSorter:
    def __init__(self, data):
        self.data = data

    def sort_by_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")
        return sorted(self.data, key=lambda x: x.get(key), reverse=True)

def main():
    sample_data = [
        {'product': 'Laptop', 'price': 1200},
        {'product': 'Smartphone', 'price': 800},
        {'product': 'Tablet', 'price': 450}
    ]
    sorter = DictSorter(sample_data)
    sorted_products = sorter.sort_by_key('price')
    print(sorted_products)

if __name__ == '__main__':
    main()