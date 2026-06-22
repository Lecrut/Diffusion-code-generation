import string

def count_special_characters(s):
    special_chars = set(string.punctuation)
    count = sum(1 for char in s if char in special_chars)
    return count, count > 0

if __name__ == '__main__':
    sample_string = "Hello, World! @#"
    result, flag = count_special_characters(sample_string)
    print(result)
    print(flag)