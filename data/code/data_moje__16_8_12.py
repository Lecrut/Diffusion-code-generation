def get_first_value(vector):
    if not vector:
        raise IndexError("The vector is empty")
    return vector[0]

if __name__ == '__main__':
    sample_vector = [42, 17, 99, 3, 71]
    result = get_first_value(sample_vector)
    print(result)