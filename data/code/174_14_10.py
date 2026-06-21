class FilterDict:
    MIN_VALUE = 0

    @staticmethod
    def filter_by_threshold(input_dict, threshold):
        return {key: value for key, value in input_dict.items() if value >= threshold}

if __name__ == '__main__':
    sample_dict = {
        "Alice": 88,
        "Bob": 95,
        "Charlie": 78,
        "David": 92
    }
    filtered_dict = FilterDict.filter_by_threshold(sample_dict, FilterDict.MIN_VALUE)
    print(f"Filtered Dictionary: {filtered_dict}")