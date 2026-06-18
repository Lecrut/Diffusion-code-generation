import sys
def main():
    text = "Hello World This is a Python Example"
    words = text.split()
    if len(words) > 1:
        print(" ".join(reversed(words)))
    return 0
if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)