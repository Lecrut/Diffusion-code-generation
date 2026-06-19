def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    reversed_chars = []
    for i in range(len(s) - 1, -1, -1):
        reversed_chars.append(s[i])
    
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud AI"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)