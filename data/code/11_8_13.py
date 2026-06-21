from collections import Counter

def find_chars_appearing_twice(text):
    counts = Counter(text)
    result = []
    for char, count in counts.items():
        if count == 2:
            result.append(char)
    result.sort()
    return result

if __name__ == '__main__':
    sample_string = "programming"
    print(find_chars_appearing_twice(sample_string))