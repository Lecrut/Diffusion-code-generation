def validate_input(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")

def count_characters(phrase):
    char_count = {}
    for char in phrase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def find_most_frequent_chars(char_count):
    max_count = max(char_count.values())
    return [char for char, count in char_count.items() if count == max_count]

def most_frequent_chars(phrase):
    validate_input(phrase)
    char_count = count_characters(phrase)
    return find_most_frequent_chars(char_count)

if __name__ == '__main__':
    sample_phrase = "hello world"
    result = most_frequent_chars(sample_phrase)
    print(result)