def compare_word_counts(list1, list2):
    from collections import Counter
    counter1 = Counter((word.lower() for word in list1))
    counter2 = Counter((word.lower() for word in list2))
    return dict(counter1 - counter2)
if __name__ == '__main__':
    sample_list1 = ['Apple', 'banana', 'Cherry']
    sample_list2 = ['apple', 'Banana', 'cherry', 'date']
    result = compare_word_counts(sample_list1, sample_list2)
    print(result)