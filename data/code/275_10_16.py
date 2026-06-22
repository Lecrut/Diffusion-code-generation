def reverse_string(s):
    reversed_str = ''
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

if __name__ == '__main__':
    sample_strings = ["data", "science", "is", "fun"]
    for s in sample_strings:
        print(reverse_string(s))