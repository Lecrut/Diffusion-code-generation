class Comparator:
    def check_equality(self, a, b):
        return a == b

if __name__ == '__main__':
    comparator = Comparator()
    result1 = comparator.check_equality(5, 5)
    result2 = comparator.check_equality('hello', 'world')
    print("Equality of 5 and 5:", result1)
    print("Equality of 'hello' and 'world':", result2)