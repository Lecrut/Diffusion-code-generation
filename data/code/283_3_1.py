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
    sample_data_str = ["apple", "banana", "cherry", "date", "elderberry"]
    def starts_with_b(s):
        return s.startswith('b')
    result2 = checker.check_elements(sample_data_str, starts_with_b)
    print(f"\nData: {sample_data_str}")
    print(f"Condition: starts with 'b'")
    print(f"Result: {result2}")