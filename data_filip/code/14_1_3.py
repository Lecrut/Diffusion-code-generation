def is_unique_characters(input_str):
    if len(input_str) > 128:
        return False
    checker = 0
    for char in input_str:
        val = ord(char)
        if checker & (1 << val) > 0:
            return False
        checker |= (1 << val)
    return True

def run_assertions():
    assert is_unique_characters("abcdef") is True
    assert is_unique_characters("abca") is False
    assert is_unique_characters("") is True
    assert is_unique_characters("a") is True
    assert is_unique_characters("The Quick Brown Fox") is False
    assert is_unique_characters("1234567890") is True
    assert is_unique_characters("AaBbCc") is True

if __name__ == '__main__':
    run_assertions()
    sample_string = "PythonProgramming"
    print(is_unique_characters(sample_string))
    sample_string = "HelloWorld"
    print(is_unique_characters(sample_string))
    sample_string = "xyz123"
    print(is_unique_characters(sample_string))