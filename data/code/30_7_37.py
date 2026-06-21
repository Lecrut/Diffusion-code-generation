def reverse_string_by_swapping(s):
    s = list(s)
    n = len(s)
    for i in range(n // 2):
        left_index = i
        right_index = n - i - 1
        while left_index < right_index:
            s[left_index], s[right_index] = s[right_index], s[left_index]
            left_index += 1
    return ''.join(s)

if __name__ == '__main__':
    sample_string = "example"
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)