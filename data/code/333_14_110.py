import re
def get_initial_chars(s):
    words = s.split()
    return ''.join(word[0] for word in words if word)
if __name__ == '__main__':
    sample_string = "Hello world, this is a test string."
    result = get_initial_chars(sample_string)
    print(result)