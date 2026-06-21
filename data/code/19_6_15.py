def run_length_encode_case_insensitive(text):
    if not text:
        return ""
    processed = text.lower()
    if not processed:
        return ""
    encoded = []
    current_char = processed[0]
    count = 1
    for char in processed[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == "__main__":
    sample_text = "AaaBbbCcccDDDD"
    result = run_length_encode_case_insensitive(sample_text)
    print(result)