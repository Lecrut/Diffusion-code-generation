import collections
def find_occurrences(sequence):
    counter = collections.Counter(sequence)
    return dict(counter)
if __name__ == '__main__':
    data = [1, 2, 3, 2, 4, 5, 2, 6, 7]
    result = find_occurrences(data)
    print(result)