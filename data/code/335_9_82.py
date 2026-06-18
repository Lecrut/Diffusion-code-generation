import sys
def main():
    text = "Hello World Python Programming"
    words_list = text.split()
    print(f"Original string: {text}")
    print(f"Split result: {words_list}")
    if len(words_list) > 0 and isinstance(words_list[0], str):
        first_word = words_list[0]
        last_word = words_list[-1]
        reversed_text = " ".join(reversed(words_list))
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Reversed text: {reversed_text}")
if __name__ == '__main__':
    main()