def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    n = len(data)
    i = 0
    while i < n:
        current_char = data[i]
        count = 1
        while i + 1 < n and data[i + 1] == current_char:
            i += 1
            count += 1
        result.append(current_char)
        result.append(str(count))
        i += 1
    return "".join(result)

if __name__ == "__main__":
    sample_input = "AAABBBCCCCDDDEE"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)