def compare_word_counts(list1, list2):
    from collections import Counter
    count1 = Counter((word.lower() for word in list1))
    count2 = Counter((word.lower() for word in list2))
    return {word: count1[word] - count2[word] for word in set(count1) | set(count2)}
if __name__ == '__main__':
    sample_list1 = ['Apple', 'banana', 'Cherry', 'apple']
    sample_list2 = ['Banana', 'cherry', 'grape', 'apple']
    result = compare_word_counts(sample_list1, sample_list2)
    print(result)