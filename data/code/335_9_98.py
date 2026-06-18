import sys
def main():
    text = "Hello World Python Programming"
    words_list = text.split()
    print("Split result:", words_list)
    if len(words_list) > 0:
        first_word, last_word = words_list[0], words_list[-1]
        reversed_first = "".join(reversed(first_word))
        reversed_last = "".join(reversed(last_word))
        print("Reversed first word:", reversed_first)
        print("Reversed last word:", reversed_last)
if __name__ == '__main__':
    main()