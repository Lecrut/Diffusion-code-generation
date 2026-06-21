class SumCalculator:
    @staticmethod
    def sum_of_numbers(numbers):
        total_sum = 0
        for number in numbers:
            total_sum += number
        return total_sum

if __name__ == '__main__':
    sample_list1 = [1, -2, 3, -4, 5]
    sample_list2 = [-10, 20, -30]
    sample_list3 = [0, 0, -5, 10]
    sample_list4 = [-1, -2, -3]

    calculator = SumCalculator()
    result1 = calculator.sum_of_numbers(sample_list1)
    result2 = calculator.sum_of_numbers(sample_list2)
    result3 = calculator.sum_of_numbers(sample_list3)
    result4 = calculator.sum_of_numbers(sample_list4)

    print(f"Sum of numbers for {sample_list1}: {result1}")
    print(f"Sum of numbers for {sample_list2}: {result2}")
    print(f"Sum of numbers for {sample_list3}: {result3}")
    print(f"Sum of numbers for {sample_list4}: {result4}")