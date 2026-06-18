import sys
def main():
    word1 = "Python"
    word2 = "Programming"
    print(f"{word1} {word2}")
if __name__ == '__main__':
    try:
        if len(sys.argv) > 0:
            word1 = sys.argv[1] if len(sys.argv) >= 2 else "Python"
            word2 = sys.argv[2] if len(sys.argv) >= 3 else "Programming"
    except Exception:
        pass
    print(f"{word1} {word2}")
if __name__ == '__main__':
    main()