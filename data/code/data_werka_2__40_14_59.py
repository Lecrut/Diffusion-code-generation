STRING_TYPE = str
EMPTY_STRING_ERROR_MESSAGE = "Input must be a non-empty string"

def get_first_letter(s):
    if not isinstance(s, STRING_TYPE) or len(s) == 0:
        raise ValueError(EMPTY_STRING_ERROR_MESSAGE)
    return s[0]

if __name__ == '__main__':
    sample_string = "Qwen, the AI assistant"
    first_letter = get_first_letter(sample_string)
    print(first_letter)