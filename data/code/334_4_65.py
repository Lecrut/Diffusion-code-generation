import sys
def main():
    word1 = "Hello"
    word2 = "World"
    print(f"{word1} {word2}")
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        sys.exit(1)