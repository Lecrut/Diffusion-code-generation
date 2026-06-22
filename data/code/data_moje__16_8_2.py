def get_first_value(vector):
    if not vector:
        raise ValueError("Vector is empty")
    return vector[0]

if __name__ == '__main__':
    sample_vector = [10, 20, 30, 40, 50]
    first_value = get_first_value(sample_vector)
    print(first_value)