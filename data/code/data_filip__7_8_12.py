import string

def count_special_characters(text):
    special_chars = set(string.punctuation)
    count = 0
    found = False
    for char in text:
        if char in special_chars:
            count += 1
            found = True
    return count, found

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Hello, World!"
    sample3 = "P@ssw0rd!#"
    print(count_special_characters(sample1))
    print(count_special_characters(sample2))
    print(count_special_characters(sample3))