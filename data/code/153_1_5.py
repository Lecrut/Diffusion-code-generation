class StringFinder:
    def __init__(self, data):
        self.data_set = set(data)

    def contains(self, target):
        return target in self.data_set

if __name__ == '__main__':
    finder1 = StringFinder([1, 2, 3, 4, 5])
    print(f"Contains 3: {finder1.contains(3)}")
    print(f"Contains 6: {finder1.contains(6)}")

    finder2 = StringFinder(['a', 'b', 'c'])
    print(f"Contains 'd': {finder2.contains('d')}")
    print(f"Contains 'b': {finder2.contains('b')}")

    finder3 = StringFinder([10, 20, 30])
    print(f"Contains 20: {finder3.contains(20)}")
    print(f"Contains 40: {finder3.contains(40)}")

    empty_finder = StringFinder([])
    print(f"Contains 5: {empty_finder.contains(5)}")