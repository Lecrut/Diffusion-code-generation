def find_middle_item(sequence):
    if not sequence:
        raise ValueError("The sequence is empty")
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print(find_middle_item(sample_list))
    except ValueError as e:
        print(e)