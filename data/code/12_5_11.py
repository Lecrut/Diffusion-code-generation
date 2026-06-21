def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    mid_index = len(sequence) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    print(get_middle_element([1, 2, 3, 4, 5]))
    print(get_middle_element([10, 20, 30]))
    print(get_middle_element([7]))
    print(get_middle_element([1, 2]))