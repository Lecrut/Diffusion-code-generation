def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_helper(substring):
        left, right = 0, len(substring) - 1
        while left < right:
            substring[left], substring[right] = substring[right], substring[left]
            left += 1
            right -= 1
    
    char_list = list(s)
    reverse_helper(char_list)
    return ''.join(char_list)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud AI"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)