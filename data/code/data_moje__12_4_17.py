def get_middle_value(sequence):
    if not sequence:
        return None
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    mid = n // 2
    if n % 2 == 1:
        return sorted_seq[mid]
    else:
        return (sorted_seq[mid - 1] + sorted_seq[mid]) / 2

if __name__ == '__main__':
    print(get_middle_value([3, 1, 2]))
    print(get_middle_value([4, 1, 3, 2]))
    print(get_middle_value([5]))
    print(get_middle_value([]))
    print(get_middle_value([7, 3, 9, 1]))