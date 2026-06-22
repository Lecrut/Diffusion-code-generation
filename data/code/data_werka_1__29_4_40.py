def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == '__main__':
    sample_value = "Hello, World!"
    print(reverse_string(sample_value))