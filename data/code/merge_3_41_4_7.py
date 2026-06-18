def main():
    # Hard-coded sample values to avoid any interactive input requirements
    original_string = "hello world this is a test string"

    # Output line 1: Original string
    print(original_string)

    # Output line 2: Fully capitalized string
    fully_capitalized = original_string.upper()
    print(fully_capitalized)

    # Output line 3: String with the first letter of every word capitalized (Title Case)
    title_cased = original_string.title()
    print(title_cased)

if __name__ == '__main__':
    main()