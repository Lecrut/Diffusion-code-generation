import sys
def main():
    word1 = "Hello"
    word2 = "World"
    print(f"{word1} {word2}")
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            input_word1 = sys.argv[1]
            input_word2 = sys.argv[2]
            print(f"{input_word1} {input_word2}")
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)
if __name__ == '__main__':
    main()