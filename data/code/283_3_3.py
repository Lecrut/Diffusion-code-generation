class ListChecker:
    def check_elements(self, data_list, condition):
        result = []
        for item in data_list:
            if condition(item):
                result.append(item)
        return result
if __name__ == '__main__':
    checker = ListChecker()
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def is_even(x):
        return x % 2 == 0
    result1 = checker.check_elements(sample_data, is_even)
    print(f"Result 1: {result1}")
    def is_greater_than_5(x):
        return x > 5
    result2 = checker.check_elements(sample_data, is_greater_than_5)
    print(f"Result 2: {result2}")
    def is_odd(x):
        return x % 2 != 0
    result3 = checker.check_elements(sample_data, is_odd)
    print(f"Result 3: {result3}")