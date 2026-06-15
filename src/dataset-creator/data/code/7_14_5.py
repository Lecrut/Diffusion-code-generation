class Comparator:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    comparator = Comparator()
    print(f"5 and 5 are equal: {comparator.check_equality(5, 5)}")
    print(f"'hello' and 'hello' are equal: {comparator.check_equality('hello', 'hello')}")
    print(f"10 and 3 are equal: {comparator.check_equality(10, 3)}")
    print(f"True and True are equal: {comparator.check_equality(True, True)}")
    print(f"5.0 and 5 are equal: {comparator.check_equality(5.0, 5)}")