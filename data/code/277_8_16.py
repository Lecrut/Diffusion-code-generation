def count_uppercase_letters(s):
    uppercase_count = 0
    for char in s:
        if char.isupper():
            uppercase_count += 1
    return uppercase_count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = count_uppercase_letters(sample_string)
    print(result)