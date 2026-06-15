import sys
if __name__ == '__main__':
    input_sentence = "This is a sample sentence"
    words = input_sentence.split()
    reversed_words = words[::-1]
    output_sentence = " ".join(reversed_words)
    print(output_sentence)