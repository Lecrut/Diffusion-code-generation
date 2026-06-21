def sort_tuples_by_second_element(tuples):
    if not all(isinstance(t, tuple) and len(t) >= 2 for t in tuples):
        raise ValueError("All elements must be tuples with at least two items")
    return sorted(tuples, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_tuples = [(1, 2), (3, 1), (5, 0)]
    sorted_tuples = sort_tuples_by_second_element(sample_tuples)
    print(sorted_tuples)