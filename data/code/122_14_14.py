class AverageCalculator:
    @staticmethod
    def calculate_average(data):
        if not data:
            return 0.0
        total = sum(data)
        count = len(data)
        return total / count

if __name__ == '__main__':
    sample_input = "10 20 30 40 50"
    input_data = sample_input.split()
    numbers = []
    error_occurred = False
    for item in input_data:
        try:
            numbers.append(float(item))
        except ValueError:
            error_occurred = True
            break
    if error_occurred:
        print("Error: Invalid input detected. Please ensure all inputs are numeric.")
    else:
        result = AverageCalculator.calculate_average(numbers)
        print(result)