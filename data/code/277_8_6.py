UPPERCASE_THRESHOLD = 65
LOWERCASE_THRESHOLD = 97

def count_uppercase_letters(s):
    count = 0
    for char in s:
        ascii_val = ord(char)
        if UPPERCASE_THRESHOLD <= ascii_val < LOWERCASE_THRESHOLD:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World!"
    print(count_uppercase_letters(sample_string))