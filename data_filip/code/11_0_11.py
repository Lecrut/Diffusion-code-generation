from collections import Counter

def find_repeated_characters(input_string):
    count = Counter(input_string)
    return [char for char, freq in count.items() if freq > 1]

if __name__ == '__main__':
    result = find_repeated_characters("programming")
    print(result)