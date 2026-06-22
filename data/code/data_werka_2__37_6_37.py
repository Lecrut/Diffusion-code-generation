def interleave_strings(str1: str, str2: str) -> str:
    return ''.join(f"{a}{b}" for a, b in zip(str1, str2))

if __name__ == '__main__':
    SAMPLE_STR1 = 'hello'
    SAMPLE_STR2 = 'world'
    result = interleave_strings(SAMPLE_STR1, SAMPLE_STR2)
    print(result)