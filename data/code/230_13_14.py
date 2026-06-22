def cumulative_sum(nums):
    return tuple(sum(nums[:i+1]) for i in range(len(nums)))

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4, 5)
    print(cumulative_sum(sample_values))