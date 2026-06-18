import sys
def main():
    word1 = "Hello"
    word2 = "World"
    result = f"{word1} {word2}"
    print(result)
    return 0
if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)