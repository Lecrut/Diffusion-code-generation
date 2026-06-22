def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    prev_char = data[0]
    for current_char in data[1:]:
        if current_char == prev_char:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            prev_char = current_char
            count = 1
    result.append(f"{count}{prev_char}")
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)