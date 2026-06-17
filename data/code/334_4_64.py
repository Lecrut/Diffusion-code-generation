import sys
def main():
    word1 = "Python"
    word2 = "Programming"
    print(f"{word1} {word2}")
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            combined = f"{sys.argv[1]}{sys.argv[2]}"
            print(combined)
        else:
            main()
    except Exception as e:
        sys.exit(1)