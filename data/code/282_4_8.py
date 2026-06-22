class SequenceCalculator:
    def calculate_sum(self, numbers):
        total = 0
        for number in numbers:
            total += number
        return total

if __name__ == '__main__':
    calculator = SequenceCalculator()
    sample_list1 = [1, 5, 10, 2]
    sample_list2 = [3, 7, 14, 6]
    print(f"The sum of {sample_list1} is: {calculator.calculate_sum(sample_list1)}")
    print(f"The sum of {sample_list2} is: {calculator.calculate_sum(sample_list2)}")