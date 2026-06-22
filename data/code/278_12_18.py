class DictFormatter:
    @staticmethod
    def format_pair(key, value):
        return f"Key: {key}, Value: {value}"

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    for key, value in sample_dict.items():
        print(DictFormatter.format_pair(key, value))