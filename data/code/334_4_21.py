import sys
def main():
    word1 = "Python"
    word2 = "Programming"
    combined_text = f"{word1} and {word2}"
    print(combined_text)
if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        word1, word2 = lines[0], lines[1]
        combined_text = f"{word1} and {word2}"
        print(combined_text)
    except FileNotFoundError:
        sys.exit(1)