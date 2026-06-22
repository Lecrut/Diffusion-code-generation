class RangeCalculator:
    @staticmethod
    def calculate_range(data):
        if not data:
            return None
        min_val = float('inf')
        max_val = float('-inf')
        for x in data:
            try:
                num = float(x)
                if num < min_val:
                    min_val = num
                if num > max_val:
                    max_val = num
            except ValueError:
                continue
        return max_val - min_val

if __name__ == '__main__':
    sample_data = [3.14159, 'a', 1.61803, 2.71828, 0.57721, 4.0, 1.0]
    range_result = RangeCalculator.calculate_range(sample_data)
    print(range_result)