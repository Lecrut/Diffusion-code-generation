def has_unique_characters(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    sample_string = "hello"
    result = has_unique_characters(sample_string)
    print(result)