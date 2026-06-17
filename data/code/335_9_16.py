import sys
def main():
    text = "Hello world Python programming is fun"
    words_list = [word for word in text.split()]
    print(f"Split result: {words_list}")
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)