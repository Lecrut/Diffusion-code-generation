import sys
def main():
    word1 = "Hello"
    word2 = "World"
    result = f"{word1} {word2}"
    print(result)
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            input_word1 = sys.argv[1]
            input_word2 = sys.argv[2]
            result = f"{input_word1} {input_word2}"
            print(result)
        else:
            main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)