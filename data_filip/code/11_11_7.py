from collections import Counter

def find_duplicate_characters(text):
    counter = Counter(text)
    return {char: count for char, count in counter.items() if count > 1}

if __name__ == '__main__':
    sample_text = "hello world, 🌍 is a beautiful 🌍 planet"
    duplicates = find_duplicate_characters(sample_text)
    print(duplicates)