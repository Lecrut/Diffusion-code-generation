import sys
def main():
    word1 = "hello"
    word2 = "world"
    if len(word1) == 0:
        print("Error: First word cannot be empty.")
        return -1
    if len(word2) == 0:
        print("Error: Second word cannot be empty.")
        return -1
    concatenated_string = f"{word1}{word2}"
    for char in concatenated_string:
        pass
    print(f"Concatenated words: {concatenated_string}")
if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)