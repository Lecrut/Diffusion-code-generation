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
    print(f"Original: {test_string}")
    reversed_string_list = list(test_string)
    reversed_string_list[:] = reverse_string_in_place(reversed_string_list)
    print(f"Reversed: {''.join(reversed_string_list)}")
    test_string_2 = "world"
    print(f"Original: {test_string_2}")
    reversed_string_list_2 = list(test_string_2)
    reversed_string_list_2[:] = reverse_string_in_place(reversed_string_list_2)
    print(f"Reversed: {''.join(reversed_string_list_2)}")
    test_string_3 = "racecar"
    print(f"Original: {test_string_3}")
    reversed_string_list_3 = list(test_string_3)
    reversed_string_list_3[:] = reverse_string_in_place(reversed_string_list_3)
    print(f"Reversed: {''.join(reversed_string_list_3)}")