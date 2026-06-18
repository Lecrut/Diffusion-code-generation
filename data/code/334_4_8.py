import sys
def main():
    word1 = "Hello"
    word2 = "World"
    combined_string = f"{word1} {word2}"
    print(combined_string)
if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines()]
            if len(lines) >= 2:
                word1, word2 = lines[0], lines[1]
                combined_string = f"{word1} {word2}"
                print(combined_string)
    except FileNotFoundError:
        fallback_word1, fallback_word2 = "Sample", "Text"
        print(fallback_word1 + " " + fallback_word2)