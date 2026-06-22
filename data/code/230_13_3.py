def cumulative_sum(numbers):
    return tuple(sum(numbers[:i+1]) for i in range(len(numbers)))

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4, 5)
    print(cumulative_sum(sample_values))