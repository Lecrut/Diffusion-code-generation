def main():
    text = "Hello, World! This is a test string for Python."
    words = [word.strip() for word in text.split()]
    print(f"Original: {text}")
    print(f"Split count: {len(words)}")
    print(f"First three words: {' '.join(words[:3])}")
if __name__ == '__main__':
    main()