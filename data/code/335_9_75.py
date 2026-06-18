def main():
    text = "Hello World Python Programming"
    words_list = text.split()
    for word in words_list:
        print(f"{word}: {len(word)} characters")
if __name__ == '__main__':
    main()