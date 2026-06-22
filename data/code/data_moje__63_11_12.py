def reverse_integer(n):
    if n < 0:
        return -int(str(-n)[::-1])
    return int(str(n)[::-1])

if __name__ == '__main__':
    test_cases = [123, -456, 0, 1200, -90, 1534236469]
    for num in test_cases:
        result = reverse_integer(num)
        print(f"Input: {num}, Reversed: {result}")