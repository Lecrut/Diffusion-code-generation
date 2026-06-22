def cumulative_sum(numbers):
    return tuple(sum(numbers[:i+1]) for i in range(len(numbers)))

if __name__ == '__main__':
    sample_values = (5, 3, 8, 2, 9)
    result = cumulative_sum(sample_values)
    print(result)