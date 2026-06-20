def filter_tuples(tuples):
    return [t for t in tuples if t[0] > 5 and t[1] < 10]

if __name__ == '__main__':
    sample_values = [(3, 7), (6, 8), (4, 9), (7, 2)]
    print(filter_tuples(sample_values))