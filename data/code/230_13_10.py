def cumulative_sum(t):
    return tuple(sum(x) for x in zip(*t))

if __name__ == '__main__':
    sample_values = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print(cumulative_sum(sample_values))