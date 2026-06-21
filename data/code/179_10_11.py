def reverse_word_order(input_string):
    words = []
    current_word = ""
    for char in input_string:
        if char != " ":
            current_word += char
        elif current_word:
            words.append(current_word)
            current_word = ""
    if current_word:
        words.append(current_word)
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_input1 = "  Hello   world this is a test "
    sample_input2 = "singleword"
    sample_input3 = "   multiple   spaces   here"
    print(f"Input: '{sample_input1}'")
    print("Output:", reverse_word_order(sample_input1))
    print("-" * 20)
    print(f"Input: '{sample_input2}'")
    print("Output:", reverse_word_order(sample_input2))
    print("-" * 20)
    print(f"Input: '{sample_input3}'")