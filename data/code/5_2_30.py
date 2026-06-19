class LengthComparator:

    def compare(self, length_a, length_b):
        if length_a > length_b:
            return 'Length A is greater than Length B.'
        elif length_a < length_b:
            return 'Length A is less than Length B.'
        else:
            return 'Length A is equal to Length B.'
if __name__ == '__main__':
    comparator = LengthComparator()
    result = comparator.compare(10, 5)
    print(result)