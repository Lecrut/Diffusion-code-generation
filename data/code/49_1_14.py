class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    @staticmethod
    def compare_lengths(len1, len2):
        if len1 > len2:
            return f"{len1} is greater than {len2}"
        elif len2 > len1:
            return f"{len2} is greater than {len1}"
        else:
            return f"{len1} is equal to {len2}"

    def compare(self):
        return LengthComparator.compare_lengths(self.length1, self.length2)

if __name__ == '__main__':
    comparator1 = LengthComparator(50, 30)
    print(comparator1.compare())
    
    comparator2 = LengthComparator(75, 75)
    print(comparator2.compare())
    
    comparator3 = LengthComparator(20, 90)
    print(comparator3.compare())