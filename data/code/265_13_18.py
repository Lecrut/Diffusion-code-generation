CHAR_COUNT = {}

def count_characters(phrase):
    for char in phrase:
        if char in CHAR_COUNT:
            CHAR_COUNT[char] += 1
        else:
            CHAR_COUNT[char] = 1

def get_most_frequent_chars():
    max_count = max(CHAR_COUNT.values())
    return [char for char, count in CHAR_COUNT.items() if count == max_count]

if __name__ == '__main__':
    sample_phrase = "hello world"
    count_characters(sample_phrase)
    result = get_most_frequent_chars()
    print(result)