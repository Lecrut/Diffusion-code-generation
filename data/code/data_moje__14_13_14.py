def get_third_element(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_element(sample_list)
    print(result)