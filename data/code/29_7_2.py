def reverse_string_in_place(s):
    n = len(s)
    left = 0
    right = n - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
if __name__ == '__main__':
    test_string = "hello"
    reversed_string = list(test_string)
    result_list = reverse_string_in_place(reversed_string)
    print("Reversed string:", "".join(result_list))
    test_string_2 = "world"
    reversed_string_2 = list(test_string_2)
    result_list_2 = reverse_string_in_place(reversed_string_2)
    print("Reversed string:", "".join(result_list_2))
    test_string_3 = "python"
    reversed_string_3 = list(test_string_3)
    result_list_3 = reverse_string_in_place(reversed_string_3)
    print("Reversed string:", "".join(result_list_3))