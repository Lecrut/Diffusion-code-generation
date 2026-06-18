import sys
def main():
    word1 = "Hello"
    word2 = "World"
    print(f"{word1} {word2}")
if __name__ == "__main__":
    try:
        with open("input.txt", "r") as f:
            input_data = f.read().strip()
            parts = input_data.split(None, 1)
            if len(parts) >= 2:
                word1 = parts[0]
                word2 = parts[1]
            else:
                print("Error: Invalid input format", file=sys.stderr)
                sys.exit(1)
        result = f"{word1} {word2}"
        if len(result) > 80:
            print(f"Warning: Output length exceeds recommended limit ({len(result)} chars)")
        print(result)
    except FileNotFoundError:
        word1 = "Hello"
        word2 = "World"
        result = f"{word1} {word2}"
        if len(result) > 80:
            print(f"Warning: Output length exceeds recommended limit ({len(result)} chars)")
        print(result)
if __name__ == "__main__":
    pass