class FilterDict:
    def __init__(self):
        self.data = {}

    def add_item(self, key, value):
        self.data[key] = value

    def filter_by_threshold(self, threshold):
        return {key: value for key, value in self.data.items() if value > threshold}

if __name__ == '__main__':
    my_filter_dict = FilterDict()
    my_filter_dict.add_item("a", 10)
    my_filter_dict.add_item("b", 20)
    my_filter_dict.add_item("c", 5)
    my_filter_dict.add_item("d", 30)

    filtered_result = my_filter_dict.filter_by_threshold(15)
    print(filtered_result)