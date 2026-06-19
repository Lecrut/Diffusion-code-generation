def reverse_string_by_swapping(s):
    s = list(s)
    n = len(s)
    
    for i in range(n // 2):
        left = i
        right = n - i - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    return ''.join(s)

if __name__ == '__main__':
    sample_string = "hello"
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)