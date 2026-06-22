def run_length_encode(text):
    if not text:
        return {}
    encoded = {}
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if current_char in encoded:
                encoded[current_char].append(count)
            else:
                encoded[current_char] = [count]
            current_char = text[i]
            count = 1
    if current_char in encoded:
        encoded[current_char].append(count)
    else:
        encoded[current_char] = [count]
    return encoded

if __name__ == '__main__':
    sample_input = "aabbbcddddeeff"
    result = run_length_encode(sample_input)
    print(result)
    sample_input_2 = "wwwwaaadexxxxxxwww"
    result_2 = run_length_encode(sample_input_2)
    print(result_2)
    empty_input = ""
    result_3 = run_length_encode(empty_input)
    print(result_3)