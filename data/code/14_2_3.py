def get_third_value(tup):
    if not tup:
        raise ValueError("Tuple is empty")
    if len(tup) < 3:
        raise IndexError("Tuple does not have a third element")
    return tup[2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    result = get_third_value(sample_tuple)
    print(result)