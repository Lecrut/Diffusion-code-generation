import collections

def find_duplicate_characters(text):
    counter = collections.Counter(text)
    duplicates = [char for char, count in counter.items() if count > 1]
    return duplicates

if __name__ == '__main__':
    sample_text = "hello world 🌍"
    result = find_duplicate_characters(sample_text)
    print(result)