def count_diff(list1, list2):
    from collections import Counter
    c1 = Counter(word.lower() for word in list1)
    c2 = Counter(word.lower() for word in list2)
    return {word: c1[word] - c2[word] for word in set(c1) | set(c2)}

if __name__ == '__main__':
    sample_list1 = ['Apple', 'banana', 'Cherry', 'apple']
    sample_list2 = ['banana', 'cherry', 'date', 'DATE']
    print(count_diff(sample_list1, sample_list2))