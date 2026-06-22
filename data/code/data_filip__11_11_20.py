import collections

def find_duplicate_characters(text):
    if not text:
        return []
    counter = collections.Counter(text)
    duplicates = [char for char, count in counter.items() if count > 1]
    return sorted(set(duplicates))

if __name__ == '__main__':
    sample_text = "Hello World! 你好 🌍"
    result = find_duplicate_characters(sample_text)
    print(result)