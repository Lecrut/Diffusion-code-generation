import sys
def main():
    word1 = "Python"
    word2 = "World"
    print(f"{word1} {word2}")
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            user_word1 = sys.argv[1]
            user_word2 = sys.argv[2]
            combined = f"{user_word1.upper()} and {user_word2.lower()}"
            print(combined)
        else:
            main()
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)