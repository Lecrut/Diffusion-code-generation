class LengthComparator:
    def compare(self, length1, length2):
        if length1 > length2:
            return "First length is greater"
        elif length1 < length2:
            return "Second length is greater"
        else:
            return "Lengths are equal"

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.compare(10, 5))
    print(comparator.compare(5, 10))
    print(comparator.compare(10, 10))