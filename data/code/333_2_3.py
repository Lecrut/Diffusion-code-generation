def main():
    sentence = "Hello world from Python"
    words = sentence.split()
    first_letters = [word[0] for word in words if len(word) > 0]
    print("".join(first_letters))
if __name__ == '__main__':
    main()