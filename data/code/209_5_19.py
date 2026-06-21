from decimal import Decimal, getcontext

class MeanCalculator:
    PRECISION = 10

    @staticmethod
    def calculate_mean(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        
        total = Decimal(0)
        count = 0
        
        for sample in data:
            total += Decimal(sample)
            count += 1
        
        return total / Decimal(count)

if __name__ == '__main__':
    getcontext().prec = MeanCalculator.PRECISION
    sample_data = [0.1, 0.2, 0.3]
    mean_value = MeanCalculator.calculate_mean(sample_data)
    print(f"Mean: {mean_value}")