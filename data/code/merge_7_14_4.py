class Comparator:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    comparator = Comparator()
    print(f"10 and 10 are equal: {comparator.check_equality(10, 10)}")
    print(f"5 and 3 are equal: {comparator.check_equality(5, 3)}")
    print(f"'hello' and 'hello' are equal: {comparator.check_equality('hello', 'hello')}")
    print(f"1.5 and 1.50 are equal: {comparator.check_equality(1.5, 1.50)}")