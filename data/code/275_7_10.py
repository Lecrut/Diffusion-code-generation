def filter_even_tuples(tuples):
    def is_second_element_even(tup):
        return tup[1] % 2 == 0

    return [t for t in tuples if is_second_element_even(t)]

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    result = filter_even_tuples(sample_data)
    print(result)