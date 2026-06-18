import sys
def main():
    word1 = "hello"
    word2 = "world"
    if not word1:
        print("Error: First word cannot be empty.")
        return 1
    if not word2:
        print("Error: Second word cannot be empty.")
        result_word = f"{word1}{word2}"
        print(result_word)
        return 0

if __name__ == '__main__':
    pass
