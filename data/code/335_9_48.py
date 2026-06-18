import sys
def main():
    text = "Hello World Python Programming"
    words_list = text.split()
    print(f"Original: {text}")
    print(f"Split result: {words_list}")
    if len(words_list) == 0:
        return 1
    for i in range(len(words_list)):
        word_count = sum(1 for char in words_list[i] if not char.isalnum())
        if word_count > 0:
            cleaned_word = [char for char in words_list[i] if char.isalnum()]
            print(f"Cleaned {i}: {''.join(cleaned_word)}")
if __name__ == '__main__':
    sys.exit(0)