def filter_tuples(tuples):
    return [t for t in tuples if t[0] > 5 and t[1] < 10]

if __name__ == '__main__':
    sample_values = [(3, 7), (8, 2), (4, 9), (6, 5)]
    filtered_values = filter_tuples(sample_values)
    print(filtered_values)