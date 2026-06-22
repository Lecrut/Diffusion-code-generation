class LengthComparator:
    def compare(self, length1, length2):
        if length1 < length2:
            result = "less than"
        elif length1 > length2:
            result = "greater than"
        else:
            result = "equal to"
        return f"Length {length1} is {result} Length {length2}"

if __name__ == '__main__':
    comparator = LengthComparator()
    print(comparator.compare(10, 20))