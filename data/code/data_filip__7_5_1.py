import string

def count_special_characters(input_string: str) -> bool:
    special_characters = set(string.punctuation)
    count = 0
    for char in input_string:
        if char in special_characters:
            count += 1
    return count > 0

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = count_special_characters(sample_input)
    print(result)