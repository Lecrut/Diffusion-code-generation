from functools import reduce

def aggregate_values(values):
    return reduce(lambda x, y: x + y, values)

if __name__ == '__main__':
    sample_data = [2, 4, 6, 8, 10]
    result = aggregate_values(sample_data)
    print(result)