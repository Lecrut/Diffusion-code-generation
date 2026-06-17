import sys
def main():
    word1 = "apple"
    word2 = "banana"
    combined = f"{word1} and {word2}"
    print(combined)
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            user_word1 = sys.argv[1]
            user_word2 = sys.argv[2]
            combined = f"{user_word1} and {user_word2}"
            print(combined)
        else:
            main()
    except Exception as e:
        pass
if __name__ == '__main__':
    try:
        word1 = "apple"
        word2 = "banana"
        combined = f"{word1} and {word2}"
        print(combined)
    except KeyboardInterrupt:
        sys.exit(0)