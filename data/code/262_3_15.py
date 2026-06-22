class StringLengthAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_min_max(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        min_len = len(min(self.data, key=len))
        max_len = len(max(self.data, key=len))
        return min_len, max_len

if __name__ == '__main__':
    analyzer = StringLengthAnalyzer(["apple", "banana", "cherry", "date"])
    min_length, max_length = analyzer.find_min_max()
    print(f"Minimum length: {min_length}")
    print(f"Maximum length: {max_length}")

    analyzer2 = StringLengthAnalyzer(["sun", "moon", "stars"])
    min_length2, max_length2 = analyzer2.find_min_max()
    print(f"Minimum length: {min_length2}")
    print(f"Maximum length: {max_length2}")