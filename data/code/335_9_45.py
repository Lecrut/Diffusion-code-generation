def main():
    text = "Hello world! This is a test sentence."
    words = [word for word in text.split()]
    print(f"Original string: {text}")
    print(f"Split result ({len(words)} items):")
    for i, w in enumerate(words):
        if i < 5 or i >= len(words) - 2:
            print(f"{i}: '{w}'")
        else:
            print(f"...{i+1}...")
if __name__ == '__main__':
    main()