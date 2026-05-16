def reverse_string_adjacent_swap(s):
    n = len(s)
    for i in range(n - 1):
        if s[i] > s[i+1]:
            s[i], s[i+1] = s[i+1], s[i]
    return s
if __name__ == '__main__':
    original_string = "cba"
    print(f"Original: {original_string}")
    result = reverse_string_adjacent_swap(list(original_string))
    print(f"Reversed: {''.join(result)}")
    original_string_2 = "fedcba"
    print(f"Original: {original_string_2}")
    result_2 = reverse_string_adjacent_swap(list(original_string_2))
    print(f"Reversed: {''.join(result_2)}")
    original_string_3 = "12345"
    print(f"Original: {original_string_3}")
    result_3 = reverse_string_adjacent_swap(list(original_string_3))
    print(f"Reversed: {''.join(result_3)}")