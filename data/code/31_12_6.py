import time
def is_palindrome_two_pointer(s: str) -> bool:
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
    result1_two = is_palindrome_two_pointer(test_string_1)
    time1 = time.perf_counter() - start_time
    print(f"Two-Pointer: {result1_two}, Time: {time1:.6f}")
    start_time = time.perf_counter()
    result1_slice = is_palindrome_slicing(test_string_1)
    time2 = time.perf_counter() - start_time
    print(f"Slicing: {result1_slice}, Time: {time2:.6f}")
    print(f"\nTesting '{test_string_2}':")
    start_time = time.perf_counter()
    result2_two = is_palindrome_two_pointer(test_string_2)
    time3 = time.perf_counter() - start_time
    print(f"Two-Pointer: {result2_two}, Time: {time3:.6f}")
    start_time = time.perf_counter()
    result2_slice = is_palindrome_slicing(test_string_2)
    time4 = time.perf_counter() - start_time
    print(f"Slicing: {result2_slice}, Time: {time4:.6f}")
    print(f"\nTesting '{test_string_3}':")
    start_time = time.perf_counter()
    result3_two = is_palindrome_two_pointer(test_string_3)
    time5 = time.perf_counter() - start_time
    print(f"Two-Pointer: {result3_two}, Time: {time5:.6f}")
    start_time = time.perf_counter()
    result3_slice = is_palindrome_slicing(test_string_3)
    time6 = time.perf_counter() - start_time
    print(f"Slicing: {result3_slice}, Time: {time6:.6f}")
    print(f"\nTesting '{test_string_4}':")
    start_time = time.perf_counter()
    result4_two = is_palindrome_two_pointer(test_string_4)
    time7 = time.perf_counter() - start_time
    print(f"Two-Pointer: {result4_two}, Time: {time7:.6f}")
    start_time = time.perf_counter()
    result4_slice = is_palindrome_slicing(test_string_4)
    time8 = time.perf_counter() - start_time
    print(f"Slicing: {result4_slice}, Time: {time8:.6f}")
    print(f"\nTesting '{test_string_5}':")
    start_time = time.perf_counter()
    result5_two = is_palindrome_two_pointer(test_string_5)
    time9 = time.perf_counter() - start_time
    print(f"Two-Pointer: {result5_two}, Time: {time9:.6f}")
    start_time = time.perf_counter()
    result5_slice = is_palindrome_slicing(test_string_5)
    time10 = time.perf_counter() - start_time
    print(f"Slicing: {result5_slice}, Time: {time10:.6f}")
    print(f"\nTesting '{test_string_6}':")
    start_time = time.perf_counter()
    result6_two = is_palindrome_two_pointer(test_string_6)
    time11 = time.perf_counter() - start_time
    print(f"Two-Pointer: {result6_two}, Time: {time11:.6f}")
    start_time = time.perf_counter()
    result6_slice = is_palindrome_slicing(test_string_6)
    time12 = time.perf_counter() - start_time
    print(f"Slicing: {result6_slice}, Time: {time12:.6f}")