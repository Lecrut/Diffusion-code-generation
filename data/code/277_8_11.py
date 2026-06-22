UPPERCASE_THRESHOLD = 65
LOWERCASE_THRESHOLD = 97

def count_uppercase_letters(s):
    count = 0
    for char in s:
        if ord(char) >= UPPERCASE_THRESHOLD and ord(char) <= LOWERCASE_THRESHOLD - 32:
            count += 1
    return count

if __name__ == '__main__':
    sample_string = "Hello World!"
    print(count_uppercase_letters(sample_string))