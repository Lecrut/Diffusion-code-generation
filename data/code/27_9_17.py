def run_length_encode(s: str) -> list:
    if not s:
        return []
    result = []
    run_cache = {"char": s[0], "count": 1}
    for char in s[1:]:
        if char == run_cache["char"]:
            run_cache["count"] += 1
        else:
            result.append((run_cache["char"], run_cache["count"]))
            run_cache["char"] = char
            run_cache["count"] = 1
    result.append((run_cache["char"], run_cache["count"]))
    return result

if __name__ == '__main__':
    sample_text = 'aabbaaccc'
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)