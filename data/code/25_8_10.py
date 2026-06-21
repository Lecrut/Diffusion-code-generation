def run_length_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aA11##@@222bbB"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)