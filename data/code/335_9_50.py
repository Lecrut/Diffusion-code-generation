import sys
def main():
    text = "Hello World Python Programming"
    words = text.split()
    if len(words) > 1:
        print(f"The first word is '{words[0]}' and the last word is '{words[-1]}'.")
        total_length = sum(len(word) for word in words)
        average_word_len = total_length / len(words) if words else 0
        print(f"Total characters: {total_length}")
        print(f"Average character length per word: {average_word_len:.2f}")
if __name__ == '__main__':
    sys.exit(0)