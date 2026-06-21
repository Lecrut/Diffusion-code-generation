class ListMatcher:

    def __init__(self, data):
        self.data = data

    def has_match(self, target):
        return any((item == target for item in self.data))
if __name__ == '__main__':
    matcher1 = ListMatcher([1, 5, 2, 5, 8, 5, 3])
    print(matcher1.has_match(5))
    print(matcher1.has_match(99))
    matcher2 = ListMatcher([10, 20, 10, 30, 10])
    print(matcher2.has_match(10))
    print(matcher2.has_match(40))
    matcher3 = ListMatcher([1, 2, 3, 4, 5])
    print(matcher3.has_match(99))