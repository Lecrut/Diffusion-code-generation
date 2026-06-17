import sys
def main():
    sentence = "Python is a great programming language"
    result = [word[0] for word in sentence.split() if word]
    print(''.join(result))
if __name__ == '__main__':
    main()