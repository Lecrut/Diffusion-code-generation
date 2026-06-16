class SequenceCalculator:
    def get_total(self, sequence):
        total = 0
        for element in sequence:
            total += element
        return total
if __name__ == '__main__':
    calculator = SequenceCalculator()
    sample_sequence = [1, 5, 10, 2]
    result = calculator.get_total(sample_sequence)
    print(result)