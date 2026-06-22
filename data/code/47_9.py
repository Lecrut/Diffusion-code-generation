from functools import reduce

def calculate_mean(values):
    return reduce(lambda acc, val: acc + val, values) / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5, 5.5]
    print(calculate_mean(sample_values))