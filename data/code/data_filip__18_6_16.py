def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result: list[str] = []
    current_char: str = data[0]
    count: int = 1
    for i in range(1, len(data)):
        char: str = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    sample: str = "aaabbcccddddd"
    encoded: str = run_length_encode(sample)
    print(encoded)