def reverse_word(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def reverse_string(s):
        return s[::-1]
    
    return reverse_string(s)

if __name__ == '__main__':
    sample_input = "Alibaba"
    try:
        reversed_output = reverse_word(sample_input)
        print(reversed_output)
    except ValueError as e:
        print(e)