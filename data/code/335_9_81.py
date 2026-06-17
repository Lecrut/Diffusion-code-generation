import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if len(words) > 1:
        print(" ".join(reversed(words)))
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)