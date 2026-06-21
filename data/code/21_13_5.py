def run_length_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(f"{text[i - 1]} {count}")
            count = 1
    result.append(f"{text[-1]} {count}")
    return " ".join(result)

if __name__ == "__main__":
    sample_text = "aaabbccccd"
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)