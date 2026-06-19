def count_frequent_letters(text):
    from collections import Counter
    char_count = Counter((char.lower() for char in text if 'a' <= char.lower() <= 'z'))
    frequent_letters = {letter: count for letter, count in char_count.items() if count > 1}
    return frequent_letters
if __name__ == '__main__':
    sample_string = 'Alibaba Cloud is a leading provider of AI and cloud services.'
    result = count_frequent_letters(sample_string)
    print(result)