class LengthComparator:
    UNIT = 'cm'

    @staticmethod
    def compare(length1, length2):
        if length1 < length2:
            return f"{length1} {LengthComparator.UNIT}"
        else:
            return f"{length2} {LengthComparator.UNIT}"

if __name__ == '__main__':
    print(LengthComparator.compare(50, 75))
    print(LengthComparator.compare(100, 80))