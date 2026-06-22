def run_length_encode(data):
    if not data:
        return ""
    result = []
    count = 1
    length = len(data)
    for i in range(length):
        if i + 1 < length and data[i] == data[i + 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(data[i])
            count = 1
    return "".join(result)

if __name__ == "__main__":
    sample_string = "aaabbccccd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)