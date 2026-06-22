def find_middle_item(sequence):
    if not sequence:
        return None
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_input = [10, 20, 30, 40, 50]
    middle_value = find_middle_item(sample_input)
    print(middle_value)