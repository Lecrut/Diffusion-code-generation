class DataTypeChecker:
    TYPE_CHECKERS = {
        float: lambda x: isinstance(x, float),
        bool: lambda x: isinstance(x, bool)
    }

    @staticmethod
    def count_non_matching_elements(data, target_type):
        non_matching_count = 0
        for item in data:
            if not DataTypeChecker.TYPE_CHECKERS[target_type](item):
                non_matching_count += 1
        return non_matching_count

if __name__ == '__main__':
    sample_data = [3.14, True, "hello", 2.718, False]
    target_type = float
    print(DataTypeChecker.count_non_matching_elements(sample_data, target_type))