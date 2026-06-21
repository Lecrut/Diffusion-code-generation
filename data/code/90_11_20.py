def has_a_or_b_prefix(texts):
    prefix_lookup = {'A': 'Alpha', 'B': 'Beta'}
    for text in texts:
        if not text:
            continue
        first_char = text[0]
        if first_char in prefix_lookup:
            return True
    return False

if __name__ == '__main__':
    words = ['Cat', 'Dog', 'Elephant']
    result = has_a_or_b_prefix(words)
    print(result)
    words_with_match = ['Cat', 'Apple', 'Dog']
    result_2 = has_a_or_b_prefix(words_with_match)
    print(result_2)