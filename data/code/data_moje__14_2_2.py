def get_third_value(tup):
    if len(tup) < 3:
        raise IndexError("Tuple must have at least three elements")
    return tup[2]

if __name__ == '__main__':
    sample_tuples = [(1, 2, 3), ('a', 'b', 'c', 'd'), (10, 20)]
    for t in sample_tuples:
        try:
            result = get_third_value(t)
            print(result)
        except IndexError as e:
            print(e)