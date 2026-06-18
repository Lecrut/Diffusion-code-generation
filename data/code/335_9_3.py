import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    print(f"Original: {text}")
    print(f"Split result: {words}")
    if len(words) > 0 and isinstance(words[0], str):
        success_message = f"Successfully split into {len(words)} words."
        sys.exit(0)
    else:
        error_message = "Failed to process input correctly."
        print(error_message)
        sys.exit(1)
if __name__ == '__main__':
    main()