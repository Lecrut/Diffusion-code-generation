from functools import reduce

def calculate_average(data):
    total = reduce(lambda x, y: x + y, data)
    average = total / len(data)
    return average

if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    print(calculate_average(sample_data))