def get_first_last_word(sentence):
    words = sentence.split()
    if len(words) < 2:
        raise ValueError("Sentence must contain at least two words.")
    return words[0], words[-1]

if __name__ == '__main__':
    sample_sentence1 = "Hello world this is a test"
    sample_sentence2 = "SingleWord"
    try:
        first, last = get_first_last_word(sample_sentence1)
        print(f"First word: {first}, Last word: {last}")
    except ValueError as e:
        print(e)

    try:
        first, last = get_first_last_word(sample_sentence2)
        print(f"First word: {first}, Last word: {last}")
    except ValueError as e:
        print(e)