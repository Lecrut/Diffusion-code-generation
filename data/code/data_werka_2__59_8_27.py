def find_middle_item(sequence):
    if not sequence:
        raise ValueError("The sequence is empty")
    middle_index = len(sequence) // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    try:
        print(find_middle_item(sample_list))
    except ValueError as e:
        print(e)