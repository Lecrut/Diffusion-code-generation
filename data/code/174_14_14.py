class DictFilter:
    MIN_VALUE = 0

    @staticmethod
    def filter_dict(input_dict):
        return {key: value for key, value in input_dict.items() if value >= DictFilter.MIN_VALUE}

if __name__ == '__main__':
    sample_dict = {
        "Alice": -5,
        "Bob": 20,
        "Charlie": 15,
        "David": 0
    }
    filtered_dict = DictFilter.filter_dict(sample_dict)
    print(f"Original Dictionary: {sample_dict}")
    print(f"Filtered Dictionary: {filtered_dict}")