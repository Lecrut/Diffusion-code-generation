from collections import Counter

def count_occurrences(data):
    return Counter(data)

if __name__ == '__main__':
    sample_list = ['red', 'blue', 'green', 'blue', 'red', 'blue']
    counts = count_occurrences(sample_list)
    print(counts)