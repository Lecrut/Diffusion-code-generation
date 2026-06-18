def main():
    sentence = "Python is a great programming language."
    words = sentence.split()
    result = [word[0] for word in words if word]
    print("".join(result))
if __name__ == '__main__':
    main()