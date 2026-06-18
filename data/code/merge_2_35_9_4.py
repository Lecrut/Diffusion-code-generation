from collections import Counter
def find_occurrences(sequence):
    counter = Counter(sequence)
    return dict(counter)
if __name__ == '__main__':
    data = [1, 2, 3, 2, 4, 5, 5, 6]
    result = find_occurrences(data)
    print(result)