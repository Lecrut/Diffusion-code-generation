class DictFilter:
    def __init__(self, data):
        self.data = data

    def filter_values(self):
        return {key: value for key, value in self.data.items() if value > 10}

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    filter_instance = DictFilter(sample_dict)
    result = filter_instance.filter_values()
    print(result)