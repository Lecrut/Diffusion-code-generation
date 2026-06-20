import string

def contains_special_characters(s):
    for char in s:
        if char not in string.ascii_letters and char not in string.digits and (char != ' '):
            return True
    return False
if __name__ == '__main__':
    test_strings = ['HelloWorld', 'Hello World!', 'Python3.8', 'NoSpacesHere']
    for test_str in test_strings:
        result = contains_special_characters(test_str)
        print(result)