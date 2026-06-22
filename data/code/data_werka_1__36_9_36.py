def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_helper(substring):
        if len(substring) <= 1:
            return substring
        mid = len(substring) // 2
        left_half = substring[:mid]
        right_half = substring[mid:]
        return reverse_helper(right_half) + reverse_helper(left_half)
    
    return reverse_helper(s)

if __name__ == '__main__':
    sample_string = "Qwen, Alibaba Cloud AI"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)