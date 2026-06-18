import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if len(words) > 1:
        print(" ".join(reversed(words)))
if __name__ == '__main__':
    try:
        sys.exit(main()) or 0
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)