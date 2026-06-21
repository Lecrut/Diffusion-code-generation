class ValueFilter:
    def __init__(self, dictionary):
        self.data = dictionary

    def filter_by_threshold(self, threshold):
        return {key: value for key, value in self.data.items() if value > threshold}

if __name__ == '__main__':
    sample_dict = {'apple': 3.50, 'banana': 2.75, 'cherry': 1.00, 'date': 4.00}
    threshold_value = 2.00
    filter_instance = ValueFilter(sample_dict)
    filtered_prices = filter_instance.filter_by_threshold(threshold_value)
    print(filtered_prices)