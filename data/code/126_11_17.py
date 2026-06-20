class NumberFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_exact_matches(self, target):
        return [num for num in self.numbers if num == target]

if __name__ == '__main__':
    finder = NumberFinder([10, 20, 30, 40, 50])
    sample_target_1 = 30
    sample_target_2 = 60

    matches_1 = finder.find_exact_matches(sample_target_1)
    matches_2 = finder.find_exact_matches(sample_target_2)

    print(matches_1)
    print(matches_2)