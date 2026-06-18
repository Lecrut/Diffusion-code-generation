import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if len(words) > 1:
        print(f"Split result: {words}")
        for i, word in enumerate(words):
            processed_word = f"{word} is the most Pythonic way to split strings."
            if len(processed_word) > 20:
                print(f"Word {i}: {processed_word}")
if __name__ == '__main__':
    main()