class TruthDetector:
    TRUE_SENTINEL = True
    FALSE_SENTINEL = False

    @staticmethod
    def detect(values):
        if not values:
            return False
        return any(values)

if __name__ == '__main__':
    test_data = [False, False, True, False]
    result = TruthDetector.detect(test_data)
    print(result)