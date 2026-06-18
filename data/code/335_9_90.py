import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if not words:
        print("Input string was empty.")
        return 1
    result_list = [word.upper() for word in words]
    joined_string = ' '.join(result_list)
    print(f"Original: {text}")
    print(f"Split count: {len(words)}")
    print(f"Joined (uppercase): {joined_string}")
if __name__ == '__main__':
    sys.exit(main())