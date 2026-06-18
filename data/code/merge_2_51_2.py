def get_first_element(sequence):
    return sequence[0] if len(sequence) > 0 else None
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_first_element(sample_list)
    print(result)