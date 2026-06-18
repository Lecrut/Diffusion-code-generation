import sys
def main():
    text = "Hello world! This is a test string."
    words_list = [word.strip().lower() for word in text.split()]
    print(f"Original: {text}")
    print(f"Split result: {words_list}")
if __name__ == '__main__':
    main()
sys.exit(0)