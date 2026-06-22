POWER_OF_TWO = 2

def cycle_and_square(numbers):
    return [num ** POWER_OF_TWO for num in numbers]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    squared_values = cycle_and_square(sample_values)
    print(squared_values)