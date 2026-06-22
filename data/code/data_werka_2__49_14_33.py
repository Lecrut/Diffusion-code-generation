class LengthComparator:
    @staticmethod
    def compare(length1, length2):
        if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
            raise ValueError("Both lengths must be numbers")
        return max(length1, length2)

if __name__ == '__main__':
    sample_length1 = 5.8
    sample_length2 = 3.4
    longer_length = LengthComparator.compare(sample_length1, sample_length2)
    print(longer_length)