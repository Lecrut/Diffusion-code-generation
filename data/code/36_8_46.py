def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')

    def reverse_helper(subs):
        if len(subs) <= 1:
            return subs
        mid = len(subs) // 2
        left_half = reverse_helper(subs[:mid])
        right_half = reverse_helper(subs[mid:])
        return right_half + left_half
    return reverse_helper(s)
if __name__ == '__main__':
    sample_string1 = 'Hello, World!'
    reversed_string1 = reverse_string(sample_string1)
    print(reversed_string1)
    sample_string2 = 'Alibaba Cloud'
    reversed_string2 = reverse_string(sample_string2)
    print(reversed_string2)
    sample_string3 = 'Qwen, the AI assistant'
    try:
        reversed_string3 = reverse_string(sample_string3)
        print(reversed_string3)
    except ValueError as e:
        print(e)