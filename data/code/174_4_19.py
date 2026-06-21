class FilteredDict:
    def __init__(self):
        self.data = {}

    def add_item(self, key, value):
        if value > 0:
            self.data[key] = value

    def filter_by_threshold(self, threshold):
        return {key: value for key, value in self.data.items() if value > threshold}

if __name__ == '__main__':
    filtered_dict_instance = FilteredDict()
    filtered_dict_instance.add_item("apple", 3.50)
    filtered_dict_instance.add_item("banana", 2.75)
    filtered_dict_instance.add_item("cherry", 1.00)
    filtered_dict_instance.add_item("date", 4.00)

    threshold_value = 2.00
    result = filtered_dict_instance.filter_by_threshold(threshold_value)
    print(result)