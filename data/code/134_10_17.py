class SetMutualExclusivityChecker:
    @staticmethod
    def check_mutual_exclusivity(set1, set2):
        return set1.isdisjoint(set2)

if __name__ == '__main__':
    sample_set_1 = {1, 2, 3}
    sample_set_2 = {4, 5, 6}
    result1 = SetMutualExclusivityChecker.check_mutual_exclusivity(sample_set_1, sample_set_2)
    print(f"Result 1: {result1}")