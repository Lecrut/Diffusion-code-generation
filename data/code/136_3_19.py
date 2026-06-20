def filter_tuples(tuples):
    return [t for t in tuples if t[0] > 5 and t[1] < 10]

if __name__ == '__main__':
    sample_data = [(3, 7), (6, 8), (9, 2), (4, 11)]
    filtered_data = filter_tuples(sample_data)
    print(filtered_data)