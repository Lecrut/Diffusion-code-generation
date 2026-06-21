class FloatProcessor:
    @staticmethod
    def sum_positive_values(float_list):
        total = 0
        for num in float_list:
            if num > 0:
                total += num
        return total

if __name__ == '__main__':
    sample_values = [1.5, -2.3, 4.8, 0.0, -1.1, 3.2]
    processor = FloatProcessor()
    result = processor.sum_positive_values(sample_values)
    print(result)