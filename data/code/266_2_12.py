from collections import defaultdict
WORD_DELIMITER = ' '

def count_words(text):
    if not text:
        return {}
    words = text.split(WORD_DELIMITER)
    word_count = defaultdict(int)
    for word in words:
        if word:
            word_count[word] += 1
    return dict(word_count)
if __name__ == '__main__':
    sample_text1 = 'This is a sample sentence for testing.'
    sample_text2 = 'Another test case with multiple words.'
    sample_text3 = ''
    sample_text4 = '   leading and trailing spaces are handled correctly.'
    count1 = count_words(sample_text1)
    print(f"Text: '{sample_text1}'")
    print(f'Word Count: {count1}\n')
    count2 = count_words(sample_text2)
    print(f"Text: '{sample_text2}'")
    print(f'Word Count: {count2}\n')
    count3 = count_words(sample_text3)
    print(f"Text: '{sample_text3}'")
    print(f'Word Count: {count3}\n')
    count4 = count_words(sample_text4)
    print(f"Text: '{sample_text4}'")
    print(f'Word Count: {count4}\n')