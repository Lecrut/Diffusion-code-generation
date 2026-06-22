def filter_even_tuples(tuples):
    filtered = []
    for t in tuples:
        if t[1] % 2 == 0:
            filtered.append(t)
    return filtered

if __name__ == '__main__':
    sample_data = [(10, 2), (3, 4), (5, 6), (7, 8)]
    result = filter_even_tuples(sample_data)
    print(result)