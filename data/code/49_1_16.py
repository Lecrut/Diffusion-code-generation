class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def compare(self):
        if self.length1 > self.length2:
            return f"{self.length1} is greater than {self.length2}"
        elif self.length1 < self.length2:
            return f"{self.length1} is less than {self.length2}"
        else:
            return f"{self.length1} is equal to {self.length2}"

if __name__ == '__main__':
    len_a = 20
    len_b = 35
    comparator_ab = LengthComparator(len_a, len_b)
    print(comparator_ab.compare())

    len_c = 70
    len_d = 70
    comparator_cd = LengthComparator(len_c, len_d)
    print(comparator_cd.compare())

    len_e = 45
    len_f = 10
    comparator_ef = LengthComparator(len_e, len_f)
    print(comparator_ef.compare())