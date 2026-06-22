def count_uppercase_letters(s):
    return sum(1 for char in s if char.isupper())

if __name__ == '__main__':
    sample_string = "Hello World!"
    print(count_uppercase_letters(sample_string))