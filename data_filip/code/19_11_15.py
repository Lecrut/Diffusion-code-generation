def run_length_encode(data: str) -> str:
    if not data:
        return ""
    encoded_parts = []
    count = 1
    length = len(data)
    for i in range(length):
        if i + 1 < length and data[i] == data[i + 1]:
            count += 1
        else:
            encoded_parts.append(f"{data[i]}{count}")
            count = 1
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    result = run_length_encode(sample_input)
    print(result)