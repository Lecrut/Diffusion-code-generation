from collections import Counter

def count_and_sort_strings(strings):
    return dict(Counter(strings).most_common())

if __name__ == '__main__':
    sample_texts = ['hello', 'world', 'hello', 'python', 'world', 'hello']
    result = count_and_sort_strings(sample_texts)
    print(result)