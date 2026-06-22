class NumberRangeCalculator:
    @staticmethod
    def calculate_range(numbers):
        if not numbers:
            return 0
        return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 15]
    sample_list2 = [42]
    sample_list3 = []
    sample_list4 = [100, 1, 50]

    calculator = NumberRangeCalculator()
    print(f"Range of {sample_list1}: {calculator.calculate_range(sample_list1)}")
    print(f"Range of {sample_list2}: {calculator.calculate_range(sample_list2)}")
    print(f"Range of {sample_list3}: {calculator.calculate_range(sample_list3)}")
    print(f"Range of {sample_list4}: {calculator.calculate_range(sample_list4)}")