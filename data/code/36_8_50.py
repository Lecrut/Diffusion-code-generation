def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')

    def reverse_helper(substring):
        return substring[::-1]
    words = s.split()
    reversed_words = [reverse_helper(word) for word in words]
    return ' '.join(reversed_words)
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