import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    print(f"Original string: {text}")
    print(f"Split result: {words}")
    if len(words) > 0 and isinstance(words[0], str):
        sys.exit(0)
    else:
        sys.exit(1)
if __name__ == '__main__':
    main()