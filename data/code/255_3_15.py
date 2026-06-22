def find_tuple_with_max_sum(tuples):
    return max(tuples, key=sum)

if __name__ == '__main__':
    sample_tuples = [(10, 5, 22, 8), (30, 15, 40, 25), (1, 50, 3)]
    result = find_tuple_with_max_sum(sample_tuples)
    print(result)