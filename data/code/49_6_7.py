class LengthComparator:
    COMPARISON_EQUAL = 'equal'
    COMPARISON_LEN1_GREATER = 'len1 is greater'
    COMPARISON_LEN2_GREATER = 'len2 is smaller'

    @staticmethod
    def compare_lengths(len1, len2):
        return (LengthComparator.COMPARISON_LEN1_GREATER if len1 > len2 else
                LengthComparator.COMPARISON_LEN2_GREATER if len1 < len2 else
                LengthComparator.COMPARISON_EQUAL)

if __name__ == '__main__':
    a = 10
    b = 10
    print(f"Comparing {a} and {b}: {LengthComparator.compare_lengths(a, b)}")
    a = 25
    b = 15
    print(f"Comparing {a} and {b}: {LengthComparator.compare_lengths(a, b)}")
    a = 5
    b = 20
    print(f"Comparing {a} and {b}: {LengthComparator.compare_lengths(a, b)}")
    a = 100
    b = 50
    print(f"Comparing {a} and {b}: {LengthComparator.compare_lengths(a, b)}")