def sort_tuples_by_second_element(tuples):
    return sorted(tuples, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_tuples = [(3, 1), (1, 2), (5, 0)]
    sorted_tuples = sort_tuples_by_second_element(sample_tuples)
    print(sorted_tuples)