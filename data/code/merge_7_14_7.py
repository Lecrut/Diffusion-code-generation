class Comparator:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    comparator = Comparator()
    result1 = comparator.check_equality(5, 5)
    print(f"5 and 5 are equal: {result1}")
    result2 = comparator.check_equality("hello", "hello")
    print(f"'hello' and 'hello' are equal: {result2}")
    result3 = comparator.check_equality(10, 20)
    print(f"10 and 20 are equal: {result3}")
    result4 = comparator.check_equality(True, True)
    print(f"True and True are equal: {result4}")
    result5 = comparator.check_equality(3.14, 3.1400000000000004)
    print(f"3.14 and 3.1400000000000004 are equal: {result5}")