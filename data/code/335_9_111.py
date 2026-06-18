import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if not words:
        print("Error: No valid input found.")
        return 1
    result_list = [word.upper() for word in words]
    joined_string = ' '.join(result_list)
    print(joined_string)
if __name__ == '__main__':
    sys.exit(main())