import sys
def main():
    word1 = "Hello"
    word2 = "World"
    combined_text = f"{word1} {word2}"
    print(combined_text)
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 3:
            user_word1 = sys.argv[1]
            user_word2 = sys.argv[2]
            combined_text = f"{user_word1} {user_word2}"
            print(combined_text)
        else:
            main()
    except Exception as e:
        print(f"Error occurred during execution. Exit code 0.")
        sys.exit(0)