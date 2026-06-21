def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_helper(subs, start, end):
        while start < end:
            subs[start], subs[end] = subs[end], subs[start]
            start += 1
            end -= 1
    
    char_list = list(s)
    reverse_helper(char_list, 0, len(char_list) - 1)
    return ''.join(char_list)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)