class LengthComparator:
    @staticmethod
    def compare(len1, len2):
        return "len1 is greater" if len1 > len2 else "len2 is smaller"

if __name__ == '__main__':
    a = 10
    b = 5
    print(f"Comparing {a} and {b}: {LengthComparator.compare(a, b)}")
    a = 7
    b = 12
    print(f"Comparing {a} and {b}: {LengthComparator.compare(a, b)}")
    a = 20
    b = 20
    print(f"Comparing {a} and {b}: {LengthComparator.compare(a, b)}")