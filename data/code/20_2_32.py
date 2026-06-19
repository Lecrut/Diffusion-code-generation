class Comparator:

    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    comp = Comparator()
    result1 = comp.check_equality(5, 5)
    result2 = comp.check_equality('hello', 'world')
    print(result1)
    print(result2)