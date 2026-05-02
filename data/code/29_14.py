import sys
def reverse_string(s):
    return s[::-1]
if __name__ == '__main__':
    sample_word = "example"
    reversed_word = reverse_string(sample_word)
    print(reversed_word)