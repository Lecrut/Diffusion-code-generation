class NumberComparator:
    @staticmethod
    def find_largest(a, b, c):
        return max(a, b, c)

if __name__ == '__main__':
    comparator = NumberComparator()
    largest_number = comparator.find_largest(10, 25, 10)
    print(f"The largest number is: {largest_number}")