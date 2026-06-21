def count_word_differences(list1, list2):
    from collections import Counter
    counter1 = Counter(word.lower() for word in list1)
    counter2 = Counter(word.lower() for word in list2)
    return dict(counter1 - counter2)

if __name__ == '__main__':
    sample_list1 = ['Apple', 'banana', 'Cherry', 'apple']
    sample_list2 = ['Banana', 'cherry', 'grape', 'apple']
    print(count_word_differences(sample_list1, sample_list2))