import sys
def main():
    text = "Hello World Python Programming"
    words_list = text.split()
    print(f"Original: {text}")
    print(f"Split result: {words_list}")
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)