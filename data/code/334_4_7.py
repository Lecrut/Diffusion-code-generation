import sys
def main():
    word1 = "hello"
    word2 = "world"
    print(f"{word1} {word2}")
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            word1 = sys.argv[1]
            word2 = sys.argv[2]
            print(f"{word1} {word2}")
        else:
            main()
    except Exception as e:
        sys.exit(1)