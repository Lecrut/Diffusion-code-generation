class ListComparator:
    _DEFAULT_SAMPLE_A = [15, 20, 5, 30]
    _DEFAULT_SAMPLE_B = [10, 25, 8, 20]

    @staticmethod
    def _get_min_length(a, b):
        return len(a) if len(a) < len(b) else len(b)

    @staticmethod
    def compare_and_print_greater(list_a, list_b):
        count = 0
        length = ListComparator._get_min_length(list_a, list_b)
        for idx in range(length):
            val_a = list_a[idx]
            val_b = list_b[idx]
            if val_a > val_b:
                print(f"{val_a} > {val_b}")
                count += 1
        return count

if __name__ == '__main__':
    sample_a = ListComparator._DEFAULT_SAMPLE_A
    sample_b = ListComparator._DEFAULT_SAMPLE_B
    total_matches = ListComparator.compare_and_print_greater(sample_a, sample_b)
    print(total_matches)