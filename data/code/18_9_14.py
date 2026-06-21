def run_length_encode(s):
    if not s:
        return ""
    result = []
    n = len(s)
    i = 0
    while i < n:
        current_char = s[i]
        count = 1
        while i + 1 < n and s[i + 1] == current_char:
            i += 1
            count += 1
        result.append(f"{count}{current_char}")
        i += 1
    return "".join(result)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)