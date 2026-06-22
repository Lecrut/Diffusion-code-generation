class RangeCalculator:
    @staticmethod
    def calculate_range(numbers):
        if not numbers:
            return 0
        minimum = min(numbers)
        maximum = max(numbers)
        return maximum - minimum

if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 15]
    range1 = RangeCalculator.calculate_range(sample_list1)
    print(f"Range of {sample_list1}: {range1}")

    sample_list2 = [42]
    range2 = RangeCalculator.calculate_range(sample_list2)
    print(f"Range of {sample_list2}: {range2}")

    sample_list3 = []
    range3 = RangeCalculator.calculate_range(sample_list3)
    print(f"Range of {sample_list3}: {range3}")