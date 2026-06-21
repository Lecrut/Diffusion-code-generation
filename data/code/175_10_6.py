def split_sentence(sentence):
    return sentence.split()
if __name__ == '__main__':
    test_sentence1 = '  hello world  '
    result1 = split_sentence(test_sentence1)
    print(f"Input: '{test_sentence1}'")
    print(f'Output: {result1}')
    test_sentence2 = 'Python   is      great'
    result2 = split_sentence(test_sentence2)
    print(f"Input: '{test_sentence2}'")
    print(f'Output: {result2}')
    test_sentence3 = 'singleword'
    result3 = split_sentence(test_sentence3)
    print(f"Input: '{test_sentence3}'")
    print(f'Output: {result3}')
    test_sentence4 = '   leading and trailing spaces   '
    result4 = split_sentence(test_sentence4)
    print(f"Input: '{test_sentence4}'")
    print(f'Output: {result4}')