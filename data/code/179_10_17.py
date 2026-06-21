def reverse_word_order(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    words = input_string.strip().split()
    reversed_words = []
    for word in words:
        if word:
            reversed_words.append(word)
    
    return " ".join(reversed_words[::-1])

if __name__ == '__main__':
    sample_input1 = "  Hello world   this is a test "
    sample_input2 = "singleword"
    sample_input3 = "   multiple   spaces   here"
    sample_input4 = ""
    sample_input5 = "   \t\n"
    
    print(f"Input: '{sample_input1}'")
    print("Output:", reverse_word_order(sample_input1))
    print("-" * 20)
    print(f"Input: '{sample_input2}'")
    print("Output:", reverse_word_order(sample_input2))
    print("-" * 20)
    print(f"Input: '{sample_input3}'")
    print("Output:", reverse_word_order(sample_input3))
    print("-" * 20)
    print(f"Input: '{sample_input4}'")
    print("Output:", reverse_word_order(sample_input4))
    print("-" * 20)
    print(f"Input: '{sample_input5}'")
    try:
        print("Output:", reverse_word_order(sample_input5))
    except ValueError as e:
        print("Error:", e)