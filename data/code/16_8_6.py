def get_first_value(vector):
    if not vector:
        raise ValueError("Vector is empty")
    return vector[0]

if __name__ == '__main__':
    sample_vector = [42, 17, 93, 6, 28]
    result = get_first_value(sample_vector)
    print(result)