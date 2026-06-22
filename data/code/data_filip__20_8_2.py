def run_length_encode(data: str) -> str:
    if not data:
        return ""
    encoded = []
    count = 1
    length = len(data)
    for i in range(length):
        if i + 1 < length and data[i] == data[i + 1]:
            count += 1
        else:
            encoded.append(str(count) + data[i])
            count = 1
    return "".join(encoded)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWWB"
    result = run_length_encode(sample_string)
    print(result)