def get_first_value(vector):
    if not vector:
        raise ValueError("Vector cannot be empty")
    return vector[0]

if __name__ == '__main__':
    sample_vector = [10, 20, 30, 40]
    result = get_first_value(sample_vector)
    print(result)