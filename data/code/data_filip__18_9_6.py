def run_length_encode_optimized(s):
    if not s:
        return ""
    result = []
    n = len(s)
    i = 0
    while i < n:
        current_char = s[i]
        count = 1
        i += 1
        while i < n and s[i] == current_char:
            count += 1
            i += 1
        result.append(str(count))
        result.append(current_char)
    return "".join(result)

if __name__ == "__main__":
    sample_string = "wwwwaaadexxxxxx"
    encoded_result = run_length_encode_optimized(sample_string)
    print(encoded_result)