class SwapValidator:
    def swap_adjacent(self, sequence, index):
        if not isinstance(sequence, (list, tuple)):
            raise TypeError("Sequence must be a list or tuple.")
        if not 0 <= index < len(sequence) - 1:
            raise IndexError(f"Index {index} is out of range for adjacent swap. Valid indices are 0 to {len(sequence)-2}.")
        sequence = list(sequence)
        value_left, value_right = sequence[index], sequence[index + 1]
        sequence[index], sequence[index + 1] = value_right, value_left
        return tuple(sequence)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    swap_obj = SwapValidator()
    try:
        result_tuple = swap_obj.swap_adjacent(sample_list, 1)
        print(f"Original List: {sample_list}")
        print(f"Swapped Tuple (indices 0 and 1): {result_tuple[0]}, {result_tuple[1]}")
        sample_tuple = (5, 6, 7, 8)
        result_from_tuple = swap_obj.swap_adjacent(sample_tuple, 2)
        print(f"\nOriginal Tuple: {sample_tuple}")
        print(f"Swapped Tuple (indices 2 and 3): {result_from_tuple[0]}, {result_from_tuple[-1]}")
    except Exception as e:
        print(f"Error occurred: {e}")