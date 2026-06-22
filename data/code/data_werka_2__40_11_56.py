def get_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[0] if s else ""

if __name__ == '__main__':
    sample_values = ["Hello", "", "World", "Python", None, 123]
    results = []
    for value in sample_values:
        try:
            results.append(get_first_letter(value))
        except ValueError as e:
            results.append(str(e))
    print(results)