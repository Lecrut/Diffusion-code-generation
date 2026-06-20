def reverse_words(sentence):
    if not sentence:
        return ""
    result = []
    current_word = []
    for char in sentence:
        if char == " ":
            if current_word:
                result.append("".join(reversed(current_word)))
                result.append(" ")
                current_word = []
        else:
            current_word.append(char)
    if current_word:
        result.append("".join(reversed(current_word)))
    return "".join(result)

if __name__ == "__main__":
    sample_input = "Hello World This Is A Test"
    output = reverse_words(sample_input)
    print(output)
    sample_input2 = "Python"
    output2 = reverse_words(sample_input2)
    print(output2)
    sample_input3 = "  Leading and trailing   "
    output3 = reverse_words(sample_input3)
    print(output3)