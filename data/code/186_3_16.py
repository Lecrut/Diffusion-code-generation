SORT_KEY_INDEX = 1

if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 1), (5, 0)]
    sorted_tuples = sorted(sample_tuples, key=lambda x: x[SORT_KEY_INDEX], reverse=True)
    print(sorted_tuples)