def find_middle_item(sequence):
    if not sequence:
        raise ValueError("The input sequence is empty.")
    n = len(sequence)
    middle_index = n // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_input = [10, 20, 30, 40, 50]
    try:
        middle_item = find_middle_item(sample_input)
        print(middle_item)
    except ValueError as e:
        print(f"Error: {e}")