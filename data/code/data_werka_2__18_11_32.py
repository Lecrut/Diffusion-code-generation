class ThresholdChecker:

    def __init__(self, threshold):
        self.threshold = threshold
        self.first_value_received = False

    def check_value(self, value):
        if not self.first_value_received:
            self.first_value_received = True
            return value > self.threshold
        else:
            return False
if __name__ == '__main__':
    checker = ThresholdChecker(10)
    print(checker.check_value(5))
    print(checker.check_value(15))
    print(checker.check_value(20))