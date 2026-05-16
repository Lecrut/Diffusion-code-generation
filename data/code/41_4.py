import sys
if __name__ == '__main__':
    input_string = "this is a sample string for testing"
    print(input_string)
    print(input_string.upper())
    print(" ".join(word.capitalize() for word in input_string.split()))