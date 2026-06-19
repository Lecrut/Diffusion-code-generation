def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == '__main__':
    sample_string = "hello"
    print(reverse_string(sample_string))