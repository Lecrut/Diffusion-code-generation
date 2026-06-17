import sys
def main():
    word1 = "Hello"
    word2 = "World"
    combined_string = f"{word1} {word2}"
    print(combined_string)
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.exit(1)