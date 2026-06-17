class ListChecker:
    def check_elements(self, data_list, condition):
        result = []
        for element in data_list:
            if condition(element):
                result.append(element)
        return result
if __name__ == '__main__':
    checker = ListChecker()
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def is_even(n):
        return n % 2 == 0
    result_even = checker.check_elements(sample_data, is_even)
    print(f"Data: {sample_data}")
    print(f"Condition (is even): {result_even}")
    sample_data_strings = ["apple", "banana", "cat", "dog", "elephant"]
    def starts_with_b(s):
        return s.startswith('b')
    result_starts_with_b = checker.check_elements(sample_data_strings, starts_with_b)
    print(f"Data: {sample_data_strings}")
    print(f"Condition (starts with 'b'): {result_starts_with_b}")
    sample_data_mixed = [10, 15, 22, 31, 40]
    def is_greater_than_12(n):
        return n > 12
    result_greater_than_12 = checker.check_elements(sample_data_mixed, is_greater_than_12)
    print(f"Data: {sample_data_mixed}")
    print(f"Condition (greater than 12): {result_greater_than_12}")