from functools import reduce

def calculate_mean(values):
    mapped = list(map(float, values))
    total = reduce(lambda x, y: x + y, mapped, 0.0)
    count = len(mapped)
    if count == 0:
        return 0.0
    return total / count

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5, 5.5]
    mean_value = calculate_mean(sample_values)
    print(mean_value)