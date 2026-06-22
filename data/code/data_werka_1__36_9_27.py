def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_substring(start, end):
        if start >= end:
            return ""
        mid = (start + end) // 2
        return reverse_substring(mid + 1, end) + s[mid] + reverse_substring(start, mid)
    
    return reverse_substring(0, len(s))

if __name__ == '__main__':
    sample_string = "Alibaba Cloud AI"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)