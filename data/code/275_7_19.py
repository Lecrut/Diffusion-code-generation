def filter_even_tuples(tuples):
    even_tuples = []
    for t in tuples:
        if t[1] % 2 == 0:
            even_tuples.append(t)
    return even_tuples

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    result = filter_even_tuples(sample_data)
    print(result)