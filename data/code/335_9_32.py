import sys
def main():
    text = "Hello world! Python is great."
    words_list = text.split()
    print(f"Original: {text}")
    print(f"Splitted count: {len(words_list)}")
    for i, word in enumerate(words_list):
        print(f"{i+1}: '{word}'")
if __name__ == '__main__':
    main()