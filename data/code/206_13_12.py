class FloatMinimizer:
    @staticmethod
    def filter_and_minimize(float_list):
        valid_numbers = [num for num in float_list if isinstance(num, (int, float))]
        return min(valid_numbers) if valid_numbers else None

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 'a', None, 0, -1]
    minimizer = FloatMinimizer()
    result = minimizer.filter_and_minimize(sample_values)
    print(result)