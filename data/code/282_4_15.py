class SumCalculator:
    def add_sequence(self, numbers):
        total = 0
        for number in numbers:
            total += number
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    sequence1 = [1, 5, 9]
    sequence2 = [12, 34, 56, 78]
    sum_sequence1 = calculator.add_sequence(sequence1)
    print(f"The sum of {sequence1} is: {sum_sequence1}")
    sum_sequence2 = calculator.add_sequence(sequence2)
    print(f"The sum of {sequence2} is: {sum_sequence2}")