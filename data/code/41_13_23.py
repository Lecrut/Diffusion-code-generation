def transform_string(text: str) -> str:
    return text.lower().swapcase()

if __name__ == '__main__':
    test_value = 'Hello World'
    result = transform_string(test_value)
    print(result)