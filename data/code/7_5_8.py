import string

def count_special_characters(input_string):
    special_characters = set(string.punctuation)
    special_characters.add(' ')
    special_characters.add('\t')
    special_characters.add('\n')
    special_characters.add('\r')
    
    count = 0
    for char in input_string:
        if char in special_characters:
            count += 1
    
    return count > 0, count

if __name__ == '__main__':
    test_string = "Hello, World! 123"
    has_special, special_count = count_special_characters(test_string)
    print(f"{has_special}, {special_count}")