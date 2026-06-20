import re

def count_special_chars(text):
    special_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    count = 0
    for char in text:
        if special_pattern.match(char):
            count += 1
    status = count > 0
    return count, status

if __name__ == '__main__':
    sample_string = "Hello, World! 123 @#"
    result_count, result_status = count_special_chars(sample_string)
    print(result_count, result_status)