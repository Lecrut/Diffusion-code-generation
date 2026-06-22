def count_words_starting_with(s, letter):
    return sum(1 for word in s.split() if word.startswith(letter))

if __name__ == '__main__':
    sample_string = "apple banana apple orange"
    starting_letter = 'a'
    print(count_words_starting_with(sample_string, starting_letter))