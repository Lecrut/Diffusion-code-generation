from functools import reduce

def compute_total(numbers):
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [7, 8, 9, 10]
    total_sum = compute_total(sample_values)
    print(total_sum)