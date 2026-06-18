def contains_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char not in seen and char.isalnum():
            seen.add(char)
        elif char in seen:
            return True
    return False
if __name__ == '__main__':
    sample_string = "Hello World"
    result = contains_repeated_chars(sample_string)
    print(f"String: '{sample_string}'")
    if result:
        print("Repeated characters found.")
    else:
        print("No repeated characters found.")