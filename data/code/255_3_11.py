def tuple_with_max_sum(tuples):
    return max(tuples, key=sum)

if __name__ == '__main__':
    sample_data = [(1, 2, 3), (4, 5, 6), (10, 11), (7,)]
    result = tuple_with_max_sum(sample_data)
    print(result)