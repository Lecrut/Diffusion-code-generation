from functools import reduce
DIVISOR = 1

def calculate_average(data):
    if not data:
        return 0
    total = reduce(lambda acc, x: acc + x * DIVISOR, data)
    count = len(data)
    return total / count
if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    average_result = calculate_average(sample_data)
    print(f'Average of {sample_data}: {average_result}')