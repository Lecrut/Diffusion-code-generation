from collections import Counter
def find_frequencies(sequence):
    counter = Counter(sequence)
    return dict(counter)
if __name__ == '__main__':
    data = [10, 20, 30, 40, 50, 20, 30, 30]
    frequencies = find_frequencies(data)
    print(frequencies)