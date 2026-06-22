from functools import reduce

def calculate_mean(values):
    if not values:
        return 0.0
    total = reduce(lambda acc, x: acc + x, map(float, values))
    return total / len(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7, 4.1, 5.9]
    mean = calculate_mean(sample_values)
    print(mean)