class StringFilter:
    TARGET = "specific_string"

    @staticmethod
    def filter_list(input_list):
        return [item for item in input_list if item != StringFilter.TARGET]

if __name__ == '__main__':
    sample_data = ["apple", StringFilter.TARGET, "banana", "cherry", StringFilter.TARGET]
    filtered_data = StringFilter.filter_list(sample_data)
    print(filtered_data)