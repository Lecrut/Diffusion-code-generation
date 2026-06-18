import sys
def main():
    text = "Hello world Python programming is fun"
    words_list = text.split()
    print(f"Original: {text}")
    print(f"Split result: {words_list}")
if __name__ == '__main__':
    main()