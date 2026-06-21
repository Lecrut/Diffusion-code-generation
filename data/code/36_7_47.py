def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_iterative(subs):
        reversed_chars = []
        for char in subs:
            reversed_chars.insert(0, char)
        return ''.join(reversed_chars)
    
    return reverse_iterative(s)

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)