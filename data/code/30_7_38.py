def reverse_string_by_swapping(s):
    s = list(s)
    def swap(i, j):
        s[i], s[j] = s[j], s[i]
    
    n = len(s)
    for i in range(n // 2):
        swap(i, n - i - 1)
    
    return ''.join(s)

if __name__ == '__main__':
    sample_string = "world"
    reversed_string = reverse_string_by_swapping(sample_string)
    print(reversed_string)