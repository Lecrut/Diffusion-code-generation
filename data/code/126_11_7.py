class ExactMatcher:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def find_exact_matches(self, target):
        return [num for num in self.numbers if num == target]

if __name__ == '__main__':
    matcher = ExactMatcher([10, 20, 30, 40, 50])
    print(matcher.find_exact_matches(30))
    print(matcher.find_exact_matches(60))