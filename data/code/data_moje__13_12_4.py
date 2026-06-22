def get_nth_element(s: str, n: int) -> str:
    if len(s) == 0:
        return ''
    normalized_index = n % len(s)
    return s[normalized_index]

if __name__ == '__main__':
    sample_string = 'hello'
    sample_index = -1
    result = get_nth_element(sample_string, sample_index)
    print(result)