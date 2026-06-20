def filter_tuples(tuples):
    return [t for t in tuples if t[0] > 5 and t[1] < 10]

if __name__ == '__main__':
    sample_tuples = [(3, 7), (6, 9), (8, 2), (4, 11)]
    filtered = filter_tuples(sample_tuples)
    print(filtered)