import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if len(words) > 1:
        print(f"{words[0]} {len(words)}")
    return True
if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        sys.stderr.write(str(e))
        sys.exit(1)