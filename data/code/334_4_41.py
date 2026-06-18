import sys
def main():
    word1 = "Python"
    word2 = "Programming"
    print(f"{word1} {word2}")
if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as f:
            input_data = [line.strip() for line in f if line.strip()]
        word1, word2 = input_data[0], input_data[1]
        print(f"{word1} {word2}")
    except FileNotFoundError:
        main()