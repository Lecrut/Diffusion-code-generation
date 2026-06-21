from collections import Counter

def find_characters_appearing_twice(text):
    char_counts = Counter(text)
    result = [char for char, count in char_counts.items() if count == 2]
    result.sort()
    return result

if __name__ == '__main__':
    sample_text = "programming"
    output = find_characters_appearing_twice(sample_text)
    print(output)