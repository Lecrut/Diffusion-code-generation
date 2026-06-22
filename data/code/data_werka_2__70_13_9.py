def get_first_last(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        raise ValueError("Input must not be empty")
    first_char = s[0]
    last_char = s[-1]
    return (first_char, last_char)

if __name__ == '__main__':
    sample_text = "OpenAI"
    result = get_first_last(sample_text)
    print(result)