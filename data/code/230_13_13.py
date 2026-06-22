def cumulative_sum(tup):
    return tuple(sum(tup[:i+1]) for i in range(len(tup)))

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(cumulative_sum(sample_tuple))