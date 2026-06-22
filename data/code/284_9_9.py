def reverse_words_in_string(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def validate_input(s):
    if not isinstance(s, str) or not s.strip():
        raise ValueError("Input must be a non-empty string")

if __name__ == '__main__':
    sample_string = "Hello world from Python"
    validate_input(sample_string)
    result = reverse_words_in_string(sample_string)
    print(result)