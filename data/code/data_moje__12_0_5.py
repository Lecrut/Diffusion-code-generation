def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        mid = length // 2
        return (sequence[mid - 1] + sequence[mid]) / 2

if __name__ == '__main__':
    print(get_middle_element([1, 3, 5]))
    print(get_middle_element([1, 2, 3, 4]))
    print(get_middle_element([42]))
    print(get_middle_element([10, 20]))