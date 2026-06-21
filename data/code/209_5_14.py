from decimal import Decimal, getcontext

class PrecisionCalculator:
    PRECISION = 10

    @staticmethod
    def calculate_mean(data):
        if not data:
            raise ValueError("Input list is empty")
        
        total = Decimal(0)
        count = Decimal(0)
        for sample in data:
            total += Decimal(sample)
            count += Decimal(1)
        
        getcontext().prec = PrecisionCalculator.PRECISION
        mean = total / count
        return mean

if __name__ == '__main__':
    sample_data = [0.1, 0.2, 0.3]
    calculator = PrecisionCalculator()
    try:
        result = calculator.calculate_mean(sample_data)
        print(f"Mean: {result}")
    except ValueError as e:
        print(e)