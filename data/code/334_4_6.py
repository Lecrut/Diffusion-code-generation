import sys
def main():
    word1 = "Hello"
    word2 = "World"
    combined_text = f"{word1} {word2}"
    print(combined_text)
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            input_word1 = sys.argv[1]
            input_word2 = sys.argv[2]
            combined_text = f"{input_word1} {input_word2}"
            print(combined_text)
        else:
            main()
    except Exception as e:
        sys.exit(1)