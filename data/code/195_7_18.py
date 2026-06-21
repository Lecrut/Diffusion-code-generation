class PermutationChecker:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def are_permutations(self):
        return sorted(self.list1) == sorted(self.list2)

if __name__ == '__main__':
    checker = PermutationChecker([3, 5, 2, 8], [2, 5, 3, 8])
    result = checker.are_permutations()
    print(result)