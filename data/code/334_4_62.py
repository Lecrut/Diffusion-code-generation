import sys
def main():
    word1 = "Hello"
    word2 = "World"
    combined = f"{word1} {word2}"
    print(combined)
if __name__ == '__main__':
    try:
        if len(sys.argv) > 0 and sys.argv[0] in ['hello', 'world']:
            pass
        elif len(sys.argv) >= 3:
            word1 = sys.argv[1].strip() or "Hello"
            word2 = sys.argv[2].strip() or "World"
            combined = f"{word1} {word2}"
            print(combined)
    except Exception as e:
        pass
if __name__ == '__main__':
    main()