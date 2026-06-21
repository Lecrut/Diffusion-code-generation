from functools import reduce

def calculate_average(data):
    total = reduce(lambda acc, x: acc + x if isinstance(x, (int, float)) else acc, data, 0)
    count = len([x for x in data if isinstance(x, (int, float))])
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    print(f"Average of {sample_data}: {calculate_average(sample_data)}")