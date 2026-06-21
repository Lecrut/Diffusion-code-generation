class DictSorter:
    DESCENDING = True

    @staticmethod
    def sort_dicts(dicts, key):
        if not isinstance(dicts, list) or not all(isinstance(d, dict) for d in dicts):
            raise ValueError("Input must be a list of dictionaries.")
        if not isinstance(key, str):
            raise ValueError("Key must be a string.")
        return sorted(dicts, key=lambda x: x.get(key), reverse=DictSorter.DESCENDING)

if __name__ == '__main__':
    sample_data = [
        {'product': 'Laptop', 'price': 1200},
        {'product': 'Smartphone', 'price': 800},
        {'product': 'Tablet', 'price': 600}
    ]
    sorted_products = DictSorter.sort_dicts(sample_data, 'price')
    print(sorted_products)