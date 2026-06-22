class LengthComparator:
    def __init__(self, length1, length2):
        self.lengths = {"length1": length1, "length2": length2}

    def compare(self):
        len1 = self.lengths["length1"]
        len2 = self.lengths["length2"]
        if len1 > len2:
            return f"{len1} is greater than {len2}"
        elif len2 > len1:
            return f"{len2} is greater than {len1}"
        else:
            return f"{len1} is equal to {len2}"

if __name__ == '__main__':
    comparator1 = LengthComparator(10, 25)
    print(comparator1.compare())
    comparator2 = LengthComparator(30, 30)
    print(comparator2.compare())
    comparator3 = LengthComparator(45, 20)
    print(comparator3.compare())