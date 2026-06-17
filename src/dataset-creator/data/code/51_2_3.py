def get_first_element(sequence):
    return sequence[0] if len(sequence) > 0 else None
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_first_element(sample_data)
    print(result)