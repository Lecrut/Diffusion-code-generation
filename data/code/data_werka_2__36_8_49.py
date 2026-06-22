def is_string_valid(s):
    return isinstance(s, str)

def reverse_string(s):
    if not is_string_valid(s):
        raise ValueError('Input must be a string')
    reversed_s = s[::-1]
    return reversed_s
if __name__ == '__main__':
    sample_string1 = 'Hello, World!'
    sample_string2 = 'Alibaba Cloud'
    sample_string3 = 'Qwen, the AI assistant'
    try:
        print(reverse_string(sample_string1))
        print(reverse_string(sample_string2))
        print(reverse_string(sample_string3))
    except ValueError as e:
        print(e)