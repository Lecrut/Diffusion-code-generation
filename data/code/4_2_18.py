def count_consonants_in_text(input_string):
    consonant_set = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    total_count = 0
    for character in input_string:
        if character in consonant_set:
            total_count += 1
    return total_count

if __name__ == '__main__':
    test_phrase = "The quick brown fox jumps over the lazy dog"
    outcome = count_consonants_in_text(test_phrase)
    print(outcome)