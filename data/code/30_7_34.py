def reverse_string_by_swapping(s):
    def swap_adjacent(i, j, arr):
        arr[i], arr[j] = arr[j], arr[i]

    s_list = list(s)
    n = len(s_list)
    
    for i in range(n // 2):
        swap_adjacent(i, n - i - 1, s_list)

    return ''.join(s_list)

if __name__ == '__main__':
    sample_string = "abcdef"
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)