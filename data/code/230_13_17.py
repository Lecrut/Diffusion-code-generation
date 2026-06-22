CUMULATIVE_SUM_START = 0

def calculate_cumulative_sum(numbers):
    return tuple(CUMULATIVE_SUM_START + sum(numbers[:i]) for i in range(len(numbers)))

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4, 5)
    print(calculate_cumulative_sum(sample_values))