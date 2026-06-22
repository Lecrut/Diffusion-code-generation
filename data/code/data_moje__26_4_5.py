class VotingEligibilityChecker:
    def __init__(self, default_threshold=18):
        self._threshold = default_threshold

    def set_threshold(self, new_threshold):
        if new_threshold < 0:
            raise ValueError("Threshold cannot be negative")
        self._threshold = new_threshold

    def check(self, age, threshold=None):
        effective_threshold = threshold if threshold is not None else self._threshold
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age >= effective_threshold

def main():
    checker = VotingEligibilityChecker()
    
    print(checker.check(20))
    
    checker.set_threshold(21)
    print(checker.check(20))
    
    print(checker.check(22, threshold=18))

if __name__ == '__main__':
    main()