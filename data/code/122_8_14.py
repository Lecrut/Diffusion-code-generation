POSITIVE_THRESHOLD = 0

def filter_and_average(numbers):
    positive_numbers = [num for num in numbers if num > POSITIVE_THRESHOLD]
    return sum(positive_numbers) / len(positive_numbers) if positive_numbers else float('nan')
if __name__ == '__main__':
    sample_values = [-10, 20, -30, 40, 50]
    average = filter_and_average(sample_values)
    print(f'The average of positive numbers is: {average}')