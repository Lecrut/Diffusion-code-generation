class KeyValueConverter:
    @staticmethod
    def convert_to_dict(pairs):
        result = {}
        for key, value in pairs:
            result[key] = value
        return result

if __name__ == '__main__':
    sample_pairs = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    converter = KeyValueConverter()
    result_dict = converter.convert_to_dict(sample_pairs)
    print(result_dict)