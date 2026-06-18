def main():
    text = "Hello world! This is a Pythonic example."
    words = text.split()
    for i in range(len(words)):
        print(f"Word {i + 1}: '{words[i]}'")
if __name__ == '__main__':
    main()