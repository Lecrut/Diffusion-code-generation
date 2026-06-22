class LengthComparator:
    @staticmethod
    def compare(length1: float, length2: float) -> float:
        if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
            return None
        return max(length1, length2)

if __name__ == '__main__':
    length_a = 5.0
    length_b = 7.5
    longer_length = LengthComparator.compare(length_a, length_b)
    print(f"The longer length is: {longer_length}")