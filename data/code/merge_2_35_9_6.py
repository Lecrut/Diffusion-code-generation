from collections import Counter
def find_frequencies(sequence):
    return dict(Counter(sequence))
if __name__ == '__main__':
    data = [10, 20, 30, 45, 10, 20, 45, 10]
    result = find_frequencies(data)
    print(result)