from collections import Counter
def find_frequencies(sequence):
    counter = Counter(sequence)
    return dict(counter)
if __name__ == '__main__':
    data = [10, 20, 30, 20, 40, 50, 20]
    result = find_frequencies(data)
    print(result)