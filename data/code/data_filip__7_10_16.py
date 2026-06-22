import re

def contains_special_char(text):
    pattern = re.compile(r'[^a-zA-Z0-9]')
    return bool(pattern.search(text))

if __name__ == '__main__':
    sample1 = "HelloWorld123"
    sample2 = "Hello@World#123"
    sample3 = "Test$Pass"
    sample4 = "NormalText"
    sample5 = "123456"
    
    print(contains_special_char(sample1))
    print(contains_special_char(sample2))
    print(contains_special_char(sample3))
    print(contains_special_char(sample4))
    print(contains_special_char(sample5))