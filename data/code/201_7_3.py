def calculate_average(numbers):
    if not numbers:
        raise ValueError('List cannot be empty')
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15, 25]
    try:
        print(f'Average of {data1}: {calculate_average(data1)}')
        print(f'Average of {data2}: {calculate_average(data2)}')
        print(f'Average of []: {calculate_average([])}')
    except ValueError as e:
        print(e)