def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_helper(subs):
        if len(subs) <= 1:
            return subs
        mid = len(subs) // 2
        left_half = reverse_helper(subs[:mid])
        right_half = reverse_helper(subs[mid:])
        return right_half + left_half
    
    return reverse_helper(s)

if __name__ == '__main__':
    sample_string = "Innovate with Alibaba Cloud"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)