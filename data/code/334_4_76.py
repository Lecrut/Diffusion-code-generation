import sys
def main():
    word1 = "hello"
    word2 = "world"
    result = f"{word1} {word2}"
    print(result)
if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            word1, word2 = lines[0], lines[1]
            result = f"{word1} {word2}"
            print(result)
    except FileNotFoundError:
        sys.exit(1)