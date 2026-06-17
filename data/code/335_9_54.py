import sys
def main():
    text = "Hello World Python Programming"
    words_list = text.split()
    print(f"Original string: {text}")
    print(f"Split result (list): {words_list}")
    for i, word in enumerate(words_list):
        if len(word) > 4:
            print(f"Word at index {i} has more than 4 characters.")
if __name__ == '__main__':
    main()