class StringFilter:
    def __init__(self, input_list):
        self.input_list = input_list

    def filter_string(self, target_string):
        return [item for item in self.input_list if item != target_string]

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "apple", "date"]
    filter_instance = StringFilter(sample_list)
    filtered_list = filter_instance.filter_string("apple")
    print(filtered_list)