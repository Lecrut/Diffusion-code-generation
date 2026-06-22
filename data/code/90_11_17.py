def contains_a_or_b_prefix(texts):
    if not isinstance(texts, (list, tuple)):
        raise TypeError("Expected a sequence of strings")
    for item in texts:
        if not isinstance(item, str):
            raise TypeError("All items must be strings")
        if len(item) == 0:
            continue
        first_char = item[0]
        if first_char == 'A' or first_char == 'B':
            return True
    return False

if __name__ == '__main__':
    words = ['Avocado', 'Banana', 'Cherry']
    output = contains_a_or_b_prefix(words)
    print(output)