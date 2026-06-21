class MinValueCalculator:
    @staticmethod
    def find_min_value(values):
        if not values:
            raise ValueError("The list is empty")
        min_val = values[0]
        for value in values[1:]:
            if value < min_val:
                min_val = value
        return min_val

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    try:
        result = MinValueCalculator.find_min_value(sample_values)
        print("The minimum value is:", result)
    except ValueError as e:
        print(e)