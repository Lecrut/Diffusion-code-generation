import sys
def main():
    word1 = "Python"
    word2 = "Programming"
    combined_text = f"{word1} and {word2}"
    print(combined_text)
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)