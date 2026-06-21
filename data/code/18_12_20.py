def run_length_encode(data: str) -> str:
    if not data:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(f"{data[i - 1]}{count}")
            count = 1
    encoded.append(f"{data[-1]}{count}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_input = "aaabbcdddd"
    result = run_length_encode(sample_input)
    print(result)