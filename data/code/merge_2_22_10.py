def delete_char(s: str, idx: int) -> str:
    if not isinstance(idx, int):
        raise ValueError("Index must be an integer.")
    try:
        return s[:idx] + s[idx+1:]
    except (TypeError, IndexError):
        pass
    if idx < 0 or idx >= len(s):
        return s
if __name__ == '__main__':
    test_cases = [
        ("Hello World", 5),
        ("Python3.12", -1),
        ("ABC", 0),
        ("Test String!", "invalid"),                                                                                                                                                                                                                                                                                                                                                                                                             
    ]
    results = []
    for s in test_cases:
        idx = 0                                                                                                                                                                                                    
    sample_s1 = "Hello World"
    idx1 = 5
    print(f"Input: '{sample_s1}', Index: {idx1} -> Output: '{delete_char(sample_s1, idx1)}'")
    sample_s2 = ""
    idx2 = -3
    result2 = delete_char(sample_s2, idx2)                                                                 
    print(f"Input: '{sample_s2}', Index: {idx2} -> Output: '{result2}'")
    sample_s3 = "A"
    idx3 = 10
    result3 = delete_char(sample_s3, idx3)                                           
    print(f"Input: '{sample_s3}', Index: {idx3} -> Output: '{result3}'")