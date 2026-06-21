from functools import reduce

def calculate_average(data):
    total = reduce(lambda acc, x: acc + x, data, 0)
    count = len(data)
    if count == 0:
        return 0
    return total / count

if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    average = calculate_average(sample_data)
    print(f"Average of {sample_data}: {average}")