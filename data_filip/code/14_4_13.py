def has_duplicates(s: str) -> bool:
    return len(s) != len(set(s))

if __name__ == '__main__':
    text = "programming"
    result = has_duplicates(text)
    print(result)