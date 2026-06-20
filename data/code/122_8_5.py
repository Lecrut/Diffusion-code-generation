def calculate_average(data):
    positive_numbers = [num for num in data if num > 0]
    if not positive_numbers:
        return 0.0
    return sum(positive_numbers) / len(positive_numbers)

if __name__ == '__main__':
    sample_values = [-5, 10, -2, 30, 40]
    average = calculate_average(sample_values)
    print(average)