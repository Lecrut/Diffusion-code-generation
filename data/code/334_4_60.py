import sys
def main():
    word1 = "Hello"
    word2 = "World"
    combined_string = f"{word1} {word2}"
    print(combined_string)
if __name__ == '__main__':
    try:
        if len(sys.argv) < 3:
            sys.exit(0)
        else:
            word1 = sys.argv[1]
            word2 = sys.argv[2]
            combined_string = f"{word1} {word2}"
            print(combined_string)
    except Exception as e:
        pass
if __name__ == '__main__':
    main()