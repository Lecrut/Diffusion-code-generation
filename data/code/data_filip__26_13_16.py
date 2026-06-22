def encode(text):
    if not text:
        return ""
    result = []
    count = 1
    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            count += 1
        else:
            result.append(f"{text[index - 1]}{count}")
            count = 1
    result.append(f"{text[-1]}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccd"
    encoded_output = encode(sample_input)
    print(encoded_output)