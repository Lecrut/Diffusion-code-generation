def main():
    text = "Hello World Python is Fun"
    words_list = text.split()
    for word in words_list:
        if len(word) > 4 and 'o' in word.lower():
            print(f"{word}: {len(word)} characters")
if __name__ == '__main__':
    main()