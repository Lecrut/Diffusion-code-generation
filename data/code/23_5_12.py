def run_length_encode(s):
    if s is None:
        raise TypeError("Input cannot be None")
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    if len(s) == 0:
        return ""
    
    result_parts = []
    idx = 0
    n = len(s)
    
    while idx < n:
        current_char = s[idx]
        count = 1
        idx += 1
        while idx < n and s[idx] == current_char:
            count += 1
            idx += 1
        result_parts.append(str(count) + current_char)
    
    return "".join(result_parts)

if __name__ == '__main__':
    test_strings = ["aaabbcccc", "a", "", "AAAAABBBB", "1223334444"]
    for text in test_strings:
        try:
            encoded = run_length_encode(text)
            print(f"Original: '{text}' -> Encoded: '{encoded}'")
        except Exception as e:
            print(f"Original: '{text}' -> Error: {e}")
    
    try:
        run_length_encode(None)
    except TypeError as err:
        print(f"None handling: {err}")
    
    try:
        run_length_encode(123)
    except TypeError as err:
        print(f"Integer handling: {err}")