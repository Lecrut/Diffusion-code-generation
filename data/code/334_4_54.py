import sys
def main():
    word1 = "Hello"
    word2 = "World"
    result = f"{word1} {word2}"
    print(result)
if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        if len(lines) >= 2:
            word1, word2 = lines[0], lines[1]
            result = f"{word1} {word2}"
            try:
                print(result)
                sys.exit(0)
            except Exception as e:
                sys.stderr.write(f"Error printing output: {e}\n")
                sys.exit(1)
        else:
            word1, word2 = "Input", "Missing"
            try:
                print(result := f"{word1} {word2}")
                sys.exit(0)
            except Exception as e:
                sys.stderr.write(f"Error printing output: {e}\n")
                sys.exit(1)
    except FileNotFoundError:
        word1, word2 = "Input", "Missing"
        try:
            print(result := f"{word1} {word2}")
            sys.exit(0)
        except Exception as e:
            sys.stderr.write(f"Error printing output: {e}\n")
            sys.exit(1)