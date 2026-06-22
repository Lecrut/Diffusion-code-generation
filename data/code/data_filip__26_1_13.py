def run_length_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    length = len(data)
    for i in range(length):
        if i + 1 < length and data[i] == data[i + 1]:
            count += 1
        else:
            result.append(data[i])
            result.append(str(count))
            count = 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbaacccccccc"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)