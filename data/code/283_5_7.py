class RangeChecker:
    @staticmethod
    def is_within_range(element, min_val, max_val):
        return min_val <= element <= max_val

    @classmethod
    def all_elements_in_range(cls, lst, min_val, max_val):
        return all(cls.is_within_range(x, min_val, max_val) for x in lst)

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9]
    min_value = 2
    max_value = 10
    result = RangeChecker.all_elements_in_range(sample_list, min_value, max_value)
    print(result)