class MeanCalculator:
    ERROR_MSG_NOT_ITERABLE = "Input is not iterable"
    ERROR_MSG_NON_NUMERIC = "Sequence contains non-numeric types"
    ERROR_MSG_EMPTY_SEQUENCE = "Empty sequence"

    @staticmethod
    def calculate_mean(sequence):
        if not hasattr(sequence, '__iter__'):
            raise ValueError(MeanCalculator.ERROR_MSG_NOT_ITERABLE)
        
        total = sum(item for item in sequence if isinstance(item, (int, float)))
        count = len([item for item in sequence if isinstance(item, (int, float))])
        
        if count == 0:
            raise ValueError(MeanCalculator.ERROR_MSG_EMPTY_SEQUENCE)
        
        return float(total / count)

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    calculator = MeanCalculator()
    print(calculator.calculate_mean(sample_sequence))