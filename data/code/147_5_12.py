def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: (x[1], x[0]))

if __name__ == '__main__':
    sample_values = [(3, 2), (1, 1), (4, 1), (2, 2)]
    print(sort_tuples(sample_values))