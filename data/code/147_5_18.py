def sort_tuples(data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("All elements must be tuples of length 2")
    return sorted(data, key=lambda x: (x[1], x[0]))

if __name__ == '__main__':
    sample_list = [(3, 5), (1, 2), (4, 4), (2, 3)]
    sorted_result = sort_tuples(sample_list)
    print(sorted_result)