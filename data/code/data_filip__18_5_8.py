def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    i = 0
    n = len(data)
    while i < n:
        char = data[i]
        count = 1
        while i + 1 < n and data[i + 1] == char:
            i += 1
            count += 1
        result.append(f"{char}{count}")
        i += 1
    return "".join(result)

if __name__ == "__main__":
    sample_empty = ""
    sample_single = "a"
    sample_normal = "aaabbbcccc"
    sample_mixed = "aabbccccddd"
    print(run_length_encode(sample_empty))
    print(run_length_encode(sample_single))
    print(run_length_encode(sample_normal))
    print(run_length_encode(sample_mixed))