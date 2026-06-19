class Comparator:

    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    comp = Comparator()
    result1 = comp.check_equality(5, 5)
    result2 = comp.check_equality('hello', 'world')
    result3 = comp.check_equality([1, 2, 3], [1, 2, 3])
    print(result1)
    print(result2)
    print(result3)