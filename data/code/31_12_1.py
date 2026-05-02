import time
def is_palindrome_two_pointers(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def is_palindrome_slicing(s: str) -> bool:
    return s == s[::-1]
if __name__ == '__main__':
    test_string_1 = "racecar"
    test_string_2 = "hello"
    test_string_3 = "madam"
    test_string_4 = "aabbaa"
    test_string_5 = ""
    test_string_6 = "level"
    print(f"Testing '{test_string_1}':")
    start_time = time.perf_counter()
    result1_two = is_palindrome_two_pointers(test_string_1)
    end_time = time.perf_counter()
    print(f"Two-Pointer Result: {result1_two}")
    print(f"Time taken: {(end_time - start_time):.6f}s\n")
    start_time = time.perf_counter()
    result1_slice = is_palindrome_slicing(test_string_1)
    end_time = time.perf_counter()
    print(f"Slicing Result: {result1_slice}")
    print(f"Time taken: {(end_time - start_time):.6f}s\n")
    print(f"Testing '{test_string_2}':")
    result2_two = is_palindrome_two_pointers(test_string_2)
    print(f"Two-Pointer Result: {result2_two}\n")
    print(f"Testing '{test_string_3}':")
    result3_two = is_palindrome_two_pointers(test_string_3)
    print(f"Two-Pointer Result: {result3_two}\n")
    print(f"Testing '{test_string_4}':")
    result4_two = is_palindrome_two_pointers(test_string_4)
    print(f"Two-Pointer Result: {result4_two}\n")
    print(f"Testing '{test_string_5}':")
    result5_two = is_palindrome_two_pointers(test_string_5)
    print(f"Two-Pointer Result: {result5_two}\n")
    print(f"Testing '{test_string_6}':")
    result6_two = is_palindrome_two_pointers(test_string_6)
    print(f"Two-Pointer Result: {result6_two}\n")