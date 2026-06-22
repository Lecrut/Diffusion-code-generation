def has_a_or_b_prefix(text_list):
    prefix_lookup = {'A': 'Alpha', 'B': 'Beta'}
    for text in text_list:
        if text and text[0] in prefix_lookup:
            return True
    return False

if __name__ == '__main__':
    words = ['Zebra', 'Ant', 'Dog']
    print(has_a_or_b_prefix(words))
    words_2 = ['Zebra', 'Dog', 'Cat']
    print(has_a_or_b_prefix(words_2))