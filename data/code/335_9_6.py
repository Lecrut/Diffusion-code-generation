import sys
def main():
    text = "Hello world! This is a test string."
    words = [word.strip() for word in text.split()]
    print(f"Original: {text}")
    print(f"Split result: {words}")
if __name__ == '__main__':
    main()
sys.exit(0)