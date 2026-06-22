class ValueFilter:
    def __init__(self, data):
        self.data = data

    def filter_values(self):
        result = {}
        for key, value in self.data.items():
            if value > 10:
                result[key] = value
        return result

if __name__ == '__main__':
    sample_dict = {
        'a': 5,
        'b': 12,
        'c': 8,
        'd': 15
    }
    filter_instance = ValueFilter(sample_dict)
    large_values = filter_instance.filter_values()
    for key, value in large_values.items():
        print(f"{key}: {value}")