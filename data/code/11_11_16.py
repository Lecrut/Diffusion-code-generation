from collections import Counter

def find_duplicate_characters(text):
    counter = Counter(text)
    duplicates = {char: count for char, count in counter.items() if count > 1}
    return duplicates
if __name__ == '__main__':
    sample_text_1 = 'hello world'
    sample_text_2 = 'abcdefg'
    sample_text_3 = 'aaabbbccc'
    sample_text_4 = '🎉🎉🎊🎊🎋'
    sample_text_5 = 'café'
    sample_text_6 = '你好世界世界'
    result_1 = find_duplicate_characters(sample_text_1)
    print(result_1)
    result_2 = find_duplicate_characters(sample_text_2)
    print(result_2)
    result_3 = find_duplicate_characters(sample_text_3)
    print(result_3)
    result_4 = find_duplicate_characters(sample_text_4)
    print(result_4)
    result_5 = find_duplicate_characters(sample_text_5)
    print(result_5)
    result_6 = find_duplicate_characters(sample_text_6)
    print(result_6)