import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if len(words) != 4:
        print("Error in word count")
        return 1
    result = f"{words[0]} {words[2]}"
    print(result)
    return 0
if __name__ == '__main__':
    sys.exit(main())