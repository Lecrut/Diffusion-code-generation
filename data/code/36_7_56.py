def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')

    def reverse_helper(subs):
        return ''.join(reversed(subs))
    return reverse_helper(s)
if __name__ == '__main__':
    SAMPLE_STRING = 'Hello, 世界!'
    try:
        REVERSED_STRING = reverse_string(SAMPLE_STRING)
        print(REVERSED_STRING)
    except ValueError as e:
        print(e)