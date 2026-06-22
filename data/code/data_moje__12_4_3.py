def get_middle_value(sequence):
    if not sequence:
        return None
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid_index = n // 2
    if n % 2 == 1:
        return sorted_seq[mid_index]
    else:
        return (sorted_seq[mid_index - 1] + sorted_seq[mid_index]) / 2

if __name__ == '__main__':
    print(get_middle_value([1, 3, 2]))
    print(get_middle_value([1, 2, 3, 4]))
    print(get_middle_value([]))
    print(get_middle_value([5]))
    print(get_middle_value([10, 2, 3, 4, 5, 6]))