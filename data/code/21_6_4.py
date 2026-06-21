def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1
    result.append(current_char + str(count))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbcccc"
    compressed_output = run_length_encode(sample_input)
    print(compressed_output)