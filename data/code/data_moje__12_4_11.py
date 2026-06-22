def middle_value(seq):
    sorted_seq = sorted(seq)
    n = len(sorted_seq)
    if n % 2 == 1:
        return sorted_seq[n // 2]
    mid_left = sorted_seq[n // 2 - 1]
    mid_right = sorted_seq[n // 2]
    return (mid_left + mid_right) / 2

if __name__ == '__main__':
    odd_list = [7, 1, 3, 9, 4]
    even_list = [7, 1, 3, 9, 4, 8]
    print(middle_value(odd_list))
    print(middle_value(even_list))