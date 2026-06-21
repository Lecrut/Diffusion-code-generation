class ListMatcher:
    def __init__(self, data):
        self.data = data

    def contains_target(self, target):
        return any(item == target for item in self.data)

if __name__ == '__main__':
    matcher1 = ListMatcher([1, 5, 2, 5, 8, 5, 3])
    print(matcher1.contains_target(5))
    print(matcher1.contains_target(99))

    matcher2 = ListMatcher([10, 20, 10, 30, 10])
    print(matcher2.contains_target(10))
    print(matcher2.contains_target(25))