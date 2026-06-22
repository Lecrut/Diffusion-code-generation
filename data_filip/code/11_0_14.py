from collections import Counter

def find_repeated_characters(s):
    counts = Counter(s)
    repeated = [char for char, count in counts.items() if count > 1]
    return repeated

if __name__ == '__main__':
    print(find_repeated_characters("programming"))
    print(find_repeated_characters("hello world"))
    print(find_repeated_characters("abc"))
    print(find_repeated_characters("aabbccdd"))