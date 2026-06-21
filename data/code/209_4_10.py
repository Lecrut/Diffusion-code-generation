from functools import reduce

def calculate_average(data):
    return reduce(lambda x, y: (x[0] + y, x[1] + 1), data, (0, 0))[0] / reduce(lambda x, y: x + 1, data, 0)

if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    print(f"Average of {sample_data}: {calculate_average(sample_data)}")