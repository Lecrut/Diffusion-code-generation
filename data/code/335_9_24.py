import sys
def main():
    text = "Hello World Python Programming"
    words = str.split(text)
    result_list = [word.capitalize() for word in words]
    print("Split Result:", result_list)
    return 0
if __name__ == '__main__':
    sys.exit(main())