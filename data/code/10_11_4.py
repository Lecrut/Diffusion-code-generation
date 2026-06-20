def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

if __name__ == '__main__':
    sample_inputs = [
        "Hello World",
        "  Hello   World  ",
        "One",
        "  ",
        "",
        "  a  b   c  "
    ]
    for sample in sample_inputs:
        print(reverse_words(sample))