class TargetFinder:
    def __init__(self, data):
        self.data_set = set(data)

    def contains(self, target):
        return target in self.data_set

if __name__ == '__main__':
    finder1 = TargetFinder([1, 2, 3, 4, 5])
    print(f"List: [1, 2, 3, 4, 5], Target: 3, Exists: {finder1.contains(3)}")
    print(f"List: [1, 2, 3, 4, 5], Target: 6, Exists: {finder1.contains(6)}")

    finder2 = TargetFinder(['a', 'b', 'c'])
    print(f"List: ['a', 'b', 'c'], Target: 'd', Exists: {finder2.contains('d')}")
    print(f"List: ['a', 'b', 'c'], Target: 'a', Exists: {finder2.contains('a')}")

    finder3 = TargetFinder([10, 20, 30])
    print(f"List: [10, 20, 30], Target: 20, Exists: {finder3.contains(20)}")
    print(f"List: [10, 20, 30], Target: 40, Exists: {finder3.contains(40)}")

    finder4 = TargetFinder([])
    print(f"List: [], Target: 5, Exists: {finder4.contains(5)}")