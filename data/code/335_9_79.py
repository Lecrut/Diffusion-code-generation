import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    print(f"Original: {text}")
    print(f"Split result: {words}")
    if len(words) > 0:
        first_word, last_word = words[0], words[-1]
        reversed_text = " ".join(reversed(words))
        print(f"Reversed order: {reversed_text}")
if __name__ == '__main__':
    main()