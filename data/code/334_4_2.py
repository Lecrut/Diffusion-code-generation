import sys
def main():
    word1 = "hello"
    word2 = "world"
    try:
        combined_string = f"{word1} {word2}"
        print(combined_string)
    except Exception as e:
        sys.exit(1)
if __name__ == '__main__':
    main()