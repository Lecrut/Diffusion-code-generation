def has_duplicates(s: str) -> bool:
    return len(s) != len(set(s))

if __name__ == '__main__':
    fixed_string = "hello"
    result = has_duplicates(fixed_string)
    print(result)