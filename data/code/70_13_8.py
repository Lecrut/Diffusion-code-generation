FIRST_CHAR_OFFSET = 0
LAST_CHAR_OFFSET = -1

def get_first_last(s: str) -> tuple:
    if len(s) == 0:
        raise ValueError("Input string must not be empty")
    first_index = FIRST_CHAR_OFFSET
    last_index = LAST_CHAR_OFFSET
    return (s[first_index], s[last_index])

if __name__ == '__main__':
    sample_text = "Python"
    result = get_first_last(sample_text)
    print(result)