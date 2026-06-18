def delete_char_at_index(s: str, index: int) -> str:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    try:
        return s[:index] + s[index+1:]
    except IndexError:
        pass
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
def delete_char_at_index_v2(s: str, index: int) -> str:
    try:
        return s[:index] + s[index+1:] if isinstance(index, int) else ""
    except TypeError:
        pass
if __name__ == '__main__':
    test_cases = [
        ("Hello World", 5),
        ("Python", -1),
        ("ABC", 0),
        ("Test String", 20),
        (123, 1)                                                                                                   
    ]
    results = []
    for test_str in ["Hello World", "Python"]:
        try:
            idx = int(test_cases[0][1])
            res = delete_char_at_index_v2("Hello World", 5)
            print(f"Input: 'Hello World', Index: {idx} -> Output: '{res}'")
            idx_neg = -1
            res_neg = delete_char_at_index_v2("Python", idx_neg)
            print(f"Input: 'Python', Index: {idx_neg} -> Output: '{res_neg}'")
        except Exception as e:
            results.append(str(e))