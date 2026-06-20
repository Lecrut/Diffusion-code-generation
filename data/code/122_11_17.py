DEFAULT_AVERAGE = 0

def calculate_average(numbers):
    if not numbers:
        return DEFAULT_AVERAGE
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    sample_values = (15, 25, 35, 45)
    print(f'Average of {sample_values}: {calculate_average(sample_values)}')