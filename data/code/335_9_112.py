import sys
def main():
    text = "Hello World Python Programming"
    words_list = text.split()
    if len(words_list) > 1:
        print(" ".join(sorted(set(words_list))))
    return 0
if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)