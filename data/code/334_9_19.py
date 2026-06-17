import sys
def main():
    word1 = "Hello"
    word2 = "World"
    result = f"{word1} {word2}"
    print(result)
if __name__ == "__main__":
    try:
        with open("input.txt", "r") as file:
            words = [line.strip() for line in file if line.strip()]
            word1, word2 = words[0], words[1]
            result = f"{word1} {word2}"
            print(result)
    except FileNotFoundError:
        sys.exit(1)