class DataTypeValidator:
    EXPECTED_TYPE = float

    @staticmethod
    def count_non_matching_elements(data):
        return sum(not isinstance(item, DataTypeValidator.EXPECTED_TYPE) for item in data)

if __name__ == '__main__':
    sample_data = [3.14, 2.718, "pi", True, False, 0.5]
    non_matching_count = DataTypeValidator.count_non_matching_elements(sample_data)
    print(non_matching_count)