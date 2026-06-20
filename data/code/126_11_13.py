class NumberMatcher:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_exact_matches(self, target):
        return [num for num in self.numbers if num == target]

if __name__ == '__main__':
    matcher = NumberMatcher([10, 20, 30, 40, 50])
    sample_target = 30
    matches = matcher.find_exact_matches(sample_target)
    print(matches)

    another_matcher = NumberMatcher([60, 70, 80, 90, 100])
    another_target = 90
    another_matches = another_matcher.find_exact_matches(another_target)
    print(another_matches)