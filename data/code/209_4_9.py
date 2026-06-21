from functools import reduce

def calculate_average(data):
    return reduce(lambda x, y: x + y, data) / len(data)

if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    print(calculate_average(sample_data))