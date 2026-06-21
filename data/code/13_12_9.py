def fetch_nth_element(s, n):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if not isinstance(n, int):
        raise TypeError("Index must be an integer")
    length = len(s)
    if length == 0:
        return None
    if n < 0:
        normalized_index = length + n
        if normalized_index < 0:
            return None
        return s[normalized_index]
    else:
        if n < length:
            return s[n]
        else:
            return None

if __name__ == '__main__':
    test_string = "Hello, World!"
    indices = [0, -1, 5, -13, 20]
    for idx in indices:
        result = fetch_nth_element(test_string, idx)
        print(f"fetch_nth_element('{test_string}', {idx}) = {result}")