def filter_tuples(tuples):
    return [t for t in tuples if t[0] > 5 and t[1] < 10]

if __name__ == '__main__':
    sample_tuples = [(6, 2), (3, 8), (7, 1), (9, 4)]
    filtered_tuples = filter_tuples(sample_tuples)
    print(filtered_tuples)