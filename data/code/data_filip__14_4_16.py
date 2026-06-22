def has_duplicate(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    text = "programming"
    print(has_duplicate(text))