class AverageCalculator:
    @staticmethod
    def is_valid_sequence(seq):
        return isinstance(seq, (list, tuple)) and all(isinstance(item, (int, float)) for item in seq)

    @staticmethod
    def compute_average(sequence):
        if not AverageCalculator.is_valid_sequence(sequence) or not sequence:
            raise ValueError("Invalid input: Expected a non-empty list of numbers")
        
        total_sum = sum(sequence)
        count = len(sequence)
        average = total_sum / count
        
        return average

if __name__ == '__main__':
    sample_values = [
        [1.0, 2.0, 3.0],
        [4, 5, 6, 7, 8],
        [-1.5, 0.0, 1.5],
        [100]
    ]

    calculator = AverageCalculator()
    
    for values in sample_values:
        try:
            avg = calculator.compute_average(values)
            print(f"Average of {values}: {avg}")
        except ValueError as e:
            print(e)