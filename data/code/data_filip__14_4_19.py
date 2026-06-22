def has_duplicates(text):
    return len(text) != len(set(text))

if __name__ == '__main__':
    sample_string = "hello"
    result = has_duplicates(sample_string)
    print(result)