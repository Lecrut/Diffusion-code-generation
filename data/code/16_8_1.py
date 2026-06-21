def get_first_value(vector):
    if not vector:
        raise ValueError("Vector cannot be empty")
    return vector[0]

if __name__ == "__main__":
    sample_vector = [42, 17, 99, 5]
    result = get_first_value(sample_vector)
    print(result)