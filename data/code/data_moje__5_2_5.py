class LengthComparator:
    def compare(self, length_a, length_b):
        if length_a is None and length_b is None:
            return "Both lengths are undefined"
        if length_a is None:
            return "Length A is undefined"
        if length_b is None:
            return "Length B is undefined"
        try:
            val_a = float(length_a)
        except (TypeError, ValueError):
            val_a = None
        try:
            val_b = float(length_b)
        except (TypeError, ValueError):
            val_b = None
        if val_a is None and val_b is None:
            return "Both values are invalid"
        if val_a is None:
            return "Length A is invalid"
        if val_b is None:
            return "Length B is invalid"
        if val_a < 0:
            raise ValueError("Length A cannot be negative")
        if val_b < 0:
            raise ValueError("Length B cannot be negative")
        if val_a == val_b:
            return "Lengths are equal"
        if val_a > val_b:
            return "Length A is longer"
        return "Length B is longer"

if __name__ == '__main__':
    comparator = LengthComparator()
    result = comparator.compare(10.5, 5.2)
    print(result)
    result2 = comparator.compare(5.2, 10.5)
    print(result2)
    result3 = comparator.compare(5.0, 5.0)
    print(result3)