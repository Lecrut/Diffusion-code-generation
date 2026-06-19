def reverse_string_by_swapping(s):
    s_list = list(s)
    n = len(s_list)
    for i in range(n // 2):
        left = i
        right = n - i - 1
        while left < right:
            s_list[left], s_list[right] = (s_list[right], s_list[left])
            left += 1
            right -= 1
    return ''.join(s_list)
if __name__ == '__main__':
    sample_string = 'abcdef'
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)