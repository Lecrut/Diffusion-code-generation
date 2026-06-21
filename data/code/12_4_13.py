def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    mid = length // 2
    if length % 2 == 0:
        return (sequence[mid - 1] + sequence[mid]) / 2
    return sequence[mid]

if __name__ == "__main__":
    odd_list = [1, 3, 5, 7, 9]
    even_list = [10, 20, 30, 40]
    empty_list = []
    print(get_middle_value(odd_list))
    print(get_middle_value(even_list))
    try:
        print(get_middle_value(empty_list))
    except ValueError as e:
        print(e)