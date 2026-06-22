class ArrayCalculator:
    DEFAULT_ARRAY = [4, 8, 12, 16]
    
    @staticmethod
    def calculate_mean(arr):
        total = sum(arr)
        count = len(arr)
        average = total / count if count != 0 else None
        return average

if __name__ == '__main__':
    sample_array = ArrayCalculator.DEFAULT_ARRAY
    result = ArrayCalculator.calculate_mean(sample_array)
    print(result)