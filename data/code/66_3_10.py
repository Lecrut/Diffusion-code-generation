def adjacent_pairs_equal(lst):
    for i in range(len(lst) - 1):
        yield lst[i] == lst[i + 1]

if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    result = list(adjacent_pairs_equal(sample_list))
    print(result)