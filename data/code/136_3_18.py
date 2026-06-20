def filter_tuples(tuples):
    return [t for t in tuples if t[0] > 5 and t[1] < 10]

if __name__ == '__main__':
    sample_tuples = [(3, 7), (6, 8), (9, 2), (4, 11)]
    filtered_tuples = filter_tuples(sample_tuples)
    print(filtered_tuples)