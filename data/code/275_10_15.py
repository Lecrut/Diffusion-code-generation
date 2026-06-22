MAX_REVERSE_LENGTH = 1024

def reverse_string(s):
    reversed_str = ''
    for char in s:
        if len(reversed_str) < MAX_REVERSE_LENGTH:
            reversed_str = char + reversed_str
        else:
            break
    return reversed_str

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "scripting"]
    for s in sample_strings:
        print(reverse_string(s))