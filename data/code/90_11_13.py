def contains_a_or_b_prefix(texts):
    if not isinstance(texts, (list, tuple)):
        raise ValueError("Input must be a list or tuple of strings")
    if not texts:
        return False
    for txt in texts:
        if not isinstance(txt, str):
            raise ValueError("Each item must be a string")
        if txt:
            first_char = txt[0]
            if first_char == 'A' or first_char == 'B':
                return True
    return False

if __name__ == '__main__':
    test_input = ['Avocado', 'Coconut', 'Banana']
    answer = contains_a_or_b_prefix(test_input)
    print(answer)