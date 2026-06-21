def reverse_string_by_swapping(s):
    def swap_adjacent(lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]

    s_list = list(s)
    n = len(s_list)
    for i in range(n // 2):
        j = n - i - 1
        while i < j:
            swap_adjacent(s_list, i, j)
            j -= 1
    return ''.join(s_list)

if __name__ == '__main__':
    sample_string = "abcdefgh"
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)