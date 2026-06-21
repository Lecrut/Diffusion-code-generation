def has_duplicates(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    text = "programming"
    result = has_duplicates(text)
    print(result)