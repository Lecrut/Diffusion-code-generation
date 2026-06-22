def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

if __name__ == '__main__':
    strings = ['hello', 'world', '!']
    for string in strings:
        print(reverse_string(string))