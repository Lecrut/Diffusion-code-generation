import sys
def main():
    sentence = "Python is easy to learn and fun."
    words = sentence.split()
    result = [word[0] for word in words if word]
    print("".join(result))
if __name__ == '__main__':
    main()