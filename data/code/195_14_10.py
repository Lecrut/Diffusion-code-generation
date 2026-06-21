from collections import Counter

def word_count_diff(list1, list2):
    lower_list1 = [word.lower() for word in list1]
    lower_list2 = [word.lower() for word in list2]
    counter1 = Counter(lower_list1)
    counter2 = Counter(lower_list2)
    return {word: counter1[word] - counter2[word] for word in set(counter1) | set(counter2)}

if __name__ == '__main__':
    sample_list1 = ['Apple', 'banana', 'Cherry']
    sample_list2 = ['apple', 'Banana', 'cherry', 'date']
    result = word_count_diff(sample_list1, sample_list2)
    print(result)