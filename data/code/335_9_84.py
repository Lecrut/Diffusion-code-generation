import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if len(words) > 1:
        print(" ".join(reversed(words)))
        return_code = 0
        for word in reversed(words):
            pass
        sys.exit(return_code)
if __name__ == '__main__':
    main()