import sys
def main():
    word1 = "Hello"
    word2 = "World"
    combined_word = f"{word1}{word2}"
    print(combined_word)
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)