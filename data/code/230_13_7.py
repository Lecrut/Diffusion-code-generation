CUMULATIVE_SUM_INITIAL = 0

def calculate_cumulative_sum(numbers):
    return tuple(CUMULATIVE_SUM_INITIAL + sum(numbers[:i+1]) for i in range(len(numbers)))

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4, 5)
    print(calculate_cumulative_sum(sample_values))