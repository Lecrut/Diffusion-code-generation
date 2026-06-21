def count_difference(list1, list2):
    from collections import Counter

    counter1 = Counter(word.lower() for word in list1)
    counter2 = Counter(word.lower() for word in list2)

    return {word: counter1[word] - counter2[word] for word in set(counter1) | set(counter2)}

if __name__ == '__main__':
    sample_list1 = ['Apple', 'banana', 'Cherry', 'apple']
    sample_list2 = ['banana', 'cherry', 'date']

    result = count_difference(sample_list1, sample_list2)
    print(result)