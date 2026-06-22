def get_third_element(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must contain at least three elements")
    return sequence[2]

if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    result = get_third_element(sample_data)
    print(result)