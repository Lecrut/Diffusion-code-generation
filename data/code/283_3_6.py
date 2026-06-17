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
    result1 = checker.check_elements(sample_data, is_even)
    print(f"Data: {sample_data}")
    print(f"Condition: is even")
    print(f"Result: {result1}")
    sample_data_strings = ["apple", "banana", "cherry", "date", "elderberry"]
    def starts_with_b(s):
        return s.startswith('b')
    result2 = checker.check_elements(sample_data_strings, starts_with_b)
    print(f"\nData: {sample_data_strings}")
    print(f"Condition: starts with 'b'")
    print(f"Result: {result2}")
    sample_data_mixed = [10, 15, 20, 25, 30]
    def is_multiple_of_5(n):
        return n % 5 == 0
    result3 = checker.check_elements(sample_data_mixed, is_multiple_of_5)
    print(f"\nData: {sample_data_mixed}")
    print(f"Condition: multiple of 5")
    print(f"Result: {result3}")