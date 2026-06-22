class LengthComparator:
    @staticmethod
    def compare_lengths(length1, length2):
        try:
            length1 = float(length1)
            length2 = float(length2)
        except ValueError:
            raise ValueError("Both inputs must be numeric values.")
        
        if length1 > length2:
            return (length1, "longer")
        elif length2 > length1:
            return (length2, "longer")
        else:
            return (length1, "equal")

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.compare_lengths(15.75, 20.33))
    print(comparator.compare_lengths(100.00, 50.50))
    print(comparator.compare_lengths(25.50, 25.50))