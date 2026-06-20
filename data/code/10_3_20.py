def reverse_words(sentence):
    if not sentence:
        return ""
    reversed_chars = []
    word_buffer = []
    for char in sentence:
        if char == " ":
            while word_buffer:
                reversed_chars.append(word_buffer.pop())
            reversed_chars.append(" ")
        else:
            word_buffer.append(char)
    while word_buffer:
        reversed_chars.append(word_buffer.pop())
    return "".join(reversed_chars)

if __name__ == "__main__":
    sample_input = "Hello World This Is A Test"
    result = reverse_words(sample_input)
    print(result)
    sample_input_2 = "Python"
    result_2 = reverse_words(sample_input_2)
    print(result_2)
    sample_input_3 = "a b c"
    result_3 = reverse_words(sample_input_3)
    print(result_3)