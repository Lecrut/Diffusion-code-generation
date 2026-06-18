import sys
def main():
    word1 = "Hello"
    word2 = "World"
    result = f"{word1} {word2}"
    print(result)
if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            input_data = file.read().strip()
        if not input_data:
            word1, word2 = "Hello", "World"
        else:
            parts = input_data.split(maxsplit=1)
            if len(parts) >= 2:
                word1, word2 = parts[0], parts[1]
            elif len(parts) == 1 and not parts[0]:
                word1, word2 = "Hello", "World"
            else:
                sys.exit(1)
        result = f"{word1} {word2}"
        print(result)
    except Exception as e:
        if isinstance(e, FileNotFoundError):
            main()
        else:
            raise
if __name__ == '__main__':
    pass