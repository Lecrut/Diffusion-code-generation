def reverse_string(s):
    def reverse_iterative(subs):
        result = []
        for char in subs:
            result.insert(0, char)
        return ''.join(result)
    
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return reverse_iterative(s)

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)