class EqualityChecker:

    @classmethod
    def are_unequal(cls, first_value, second_value):
        return first_value != second_value
if __name__ == '__main__':
    value1 = 42
    value2 = 75
    result1 = EqualityChecker.are_unequal(value1, value2)
    print(f'Are {value1} and {value2} unequal? {result1}')
    string_a = 'Python'
    string_b = 'Java'
    result2 = EqualityChecker.are_unequal(string_a, string_b)
    print(f"Are '{string_a}' and '{string_b}' unequal? {result2}")
    float_x = 3.14
    float_y = 3.14159
    result3 = EqualityChecker.are_unequal(float_x, float_y)
    print(f'Are {float_x} and {float_y} unequal? {result3}')