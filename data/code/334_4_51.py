import sys
def main():
    word1 = "hello"
    word2 = "world"
    combined_string = f"{word1} {word2}"
    print(combined_string)
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            word1 = sys.argv[1]
            word2 = sys.argv[2]
            combined_string = f"{word1} {word2}"
            print(combined_string)
        else:
            main()
    except Exception as e:
        sys.exit(1)