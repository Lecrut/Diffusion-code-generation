def get_last_element(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    return sequence[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    try:
        result = get_last_element(sample_list)
        print(f"The last element is {result}")
    except ValueError as e:
        print(e)