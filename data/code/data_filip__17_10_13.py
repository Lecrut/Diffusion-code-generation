def run_length_encode(data):
    if not data:
        return ""
    iterator = iter(data)
    try:
        current_char = next(iterator)
    except StopIteration:
        return ""
    count = 1
    result = []
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDEEFFFF"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)