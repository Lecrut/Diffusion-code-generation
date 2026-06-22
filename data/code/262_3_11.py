class StringLengthAnalyzer:
    MIN_LENGTH = 0
    MAX_LENGTH = float('inf')

    @staticmethod
    def find_min_max(data):
        if not data:
            raise ValueError("Input iterable cannot be empty")
        
        minimum = min(data, key=len)
        maximum = max(data, key=len)
        
        return minimum, maximum

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date", "elderberry"]
    min_val, max_val = StringLengthAnalyzer.find_min_max(sample_data)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")

    sample_data_2 = ["one", "two", "three", "four", "five"]
    min_val_2, max_val_2 = StringLengthAnalyzer.find_min_max(sample_data_2)
    print(f"Minimum: {min_val_2}")
    print(f"Maximum: {max_val_2}")