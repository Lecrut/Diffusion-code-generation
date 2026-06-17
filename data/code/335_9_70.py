import sys
def main():
    text = "Hello world! Python is awesome."
    words_list = [word for word in text.split() if len(word) > 1]
    print("Split result:", words_list)
if __name__ == '__main__':
    try:
        sys.exit(main()) or 0
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)