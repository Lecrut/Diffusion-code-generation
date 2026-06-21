def compare_word_counts(list1, list2):
    from collections import Counter
    count1 = Counter((word.lower() for word in list1))
    count2 = Counter((word.lower() for word in list2))
    return dict(count1 - count2)
if __name__ == '__main__':
    sample_list1 = ['Apple', 'Banana', 'apple', 'Cherry']
    sample_list2 = ['banana', 'cherry', 'cherry', 'date']
    result = compare_word_counts(sample_list1, sample_list2)
    print(result)