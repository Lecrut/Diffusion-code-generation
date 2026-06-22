class MedianCalculator:
    @staticmethod
    def find_median(data):
        data.sort()
        n = len(data)
        if n == 0:
            return None
        elif n % 2 == 1:
            return data[n // 2]
        else:
            mid1 = data[n // 2 - 1]
            mid2 = data[n // 2]
            return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_data = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    calculator = MedianCalculator()
    median_value = calculator.find_median(sample_data)
    print(median_value)