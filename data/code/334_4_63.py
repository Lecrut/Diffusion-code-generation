import sys
def main():
    word1 = "hello"
    word2 = "world"
    if len(word1) != len(word2):
        print("Error: Words must be of equal length.")
        return 0
    combined = f"{word1}{word2}"
    print(combined.upper())
if __name__ == '__main__':
    exit(main() or 0)