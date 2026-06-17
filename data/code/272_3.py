import sys
if __name__ == '__main__':
    input_string = "apple banana cherry date elderberry"
    words = input_string.split()
    words.sort()
    print(" ".join(words))