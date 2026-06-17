def main():
    sentence = "Hello World Python Programming"
    words = sentence.split()
    result = [word[0] for word in words if len(word) > 0]
    print("".join(result))
if __name__ == '__main__':
    main()