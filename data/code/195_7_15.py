class PermutationValidator:
    def __init__(self, list1, list2):
        self.list1 = sorted(list1)
        self.list2 = sorted(list2)

    def are_permutations(self):
        return self.list1 == self.list2

if __name__ == '__main__':
    validator = PermutationValidator([3, 5, 2, 8], [2, 5, 3, 8])
    print(validator.are_permutations())