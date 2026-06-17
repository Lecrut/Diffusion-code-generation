import sys
def main():
    sentence = "Hello World Python Programming"
    words = sentence.split()
    for word in words:
        if word.strip():
            print(word[0])
if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)