import sys
def main():
    text = "Hello world! This is a Pythonic example."
    words = [word.strip() for word in text.split()]
    if len(words) > 0:
        print(f"First word: {words[0]}")
        print("Total count:", len(words))
if __name__ == '__main__':
    main()