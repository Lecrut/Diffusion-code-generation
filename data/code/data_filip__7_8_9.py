def count_special_characters(s):
    special_characters = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    count = 0
    for char in s:
        if char in special_characters:
            count += 1
    return count, count > 0

if __name__ == '__main__':
    sample_string = "Hello, World! 123 @#"
    result, status = count_special_characters(sample_string)
    print(result, status)