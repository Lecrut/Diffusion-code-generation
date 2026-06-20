class NegativeValueDetector:
    def detect_negative(self, value):
        return value < 0

if __name__ == '__main__':
    detector = NegativeValueDetector()
    sample_values = [10, -5, 0, -100, 3.14]
    for value in sample_values:
        result = detector.detect_negative(value)
        print(f"Value: {value}, Is Negative: {result}")