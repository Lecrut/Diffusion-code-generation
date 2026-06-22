def tuple_with_highest_sum(tuples):
    return max(tuples, key=sum)

if __name__ == '__main__':
    sample_data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11)]
    print(tuple_with_highest_sum(sample_data))