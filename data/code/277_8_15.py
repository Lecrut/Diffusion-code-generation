UPPERCASE_THRESHOLD = 65
LOWERCASE_THRESHOLD = 97
ALPHABET_SIZE = 26

def count_uppercase_letters(s):
    count = 0
    for char in s:
        ascii_val = ord(char)
        if UPPERCASE_THRESHOLD <= ascii_val < LOWERCASE_THRESHOLD + ALPHABET_SIZE:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World!"
    uppercase_count = count_uppercase_letters(sample_string)
    print(uppercase_count)