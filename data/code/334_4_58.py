import sys
def main():
    word1 = "Hello"
    word2 = "World"
    combined_word = f"{word1} {word2}"
    print(combined_word)
if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            if len(lines) >= 2:
                word1, word2 = lines[0], lines[1]
                combined_word = f"{word1} {word2}"
                print(combined_word)
    except FileNotFoundError:
        sys.exit(1)