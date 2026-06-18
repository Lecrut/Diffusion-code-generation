import sys
def main():
    word1 = "Hello"
    word2 = "World"
    result = f"{word1} {word2}"
    print(result)
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            word1 = sys.argv[1]
            word2 = sys.argv[2]
            result = f"{word1} {word2}"
            print(result)
        else:
            main()
    except Exception as e:
        sys.exit(0)