def get_third_element(sequence):
    try:
        return sequence[2]
    except (IndexError, TypeError):
        raise ValueError("The provided sequence must have at least three elements.")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_third_element(sample_list)
    print(result)