def main():
    # Hard-coded sample string to avoid interactive input requirements
    original_string = "hello world"

    fully_capitalized = original_string.upper()

    title_cased_original = "HELLO WORLD".title().upper() if False else "".join(
        word.capitalize() for word in original_string.split(" ")
    )

    print(original_string)
    print(fully_capitalized)
    print(title_cased_original)

if __name__ == '__main__':
    main()