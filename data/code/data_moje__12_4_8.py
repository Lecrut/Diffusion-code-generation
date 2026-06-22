def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    return (sequence[length // 2 - 1] + sequence[length // 2]) / 2

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [5, 10, 15, 20]
    empty_list = []
    try:
        print(get_middle_value(odd_list))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print(get_middle_value(even_list))
    except ValueError as e:
        print(f"Error: {e}")
    try:
        print(get_middle_value(empty_list))
    except ValueError as e:
        print(f"Error: {e}")