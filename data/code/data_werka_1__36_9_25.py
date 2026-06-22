def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_helper(sub_s):
        char_list = list(sub_s)
        left, right = 0, len(char_list) - 1
        while left < right:
            char_list[left], char_list[right] = char_list[right], char_list[left]
            left += 1
            right -= 1
        return ''.join(char_list)
    
    return reverse_helper(s)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud AI"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)