def main():
    # Hard-coded sample string to simulate input without using sys.stdin or input()
    original_string = "hello world this is a test"

    # Output line 1: Original string
    print(original_string)

    # Output line 2: Fully capitalized string
    fully_capitalized = original_string.upper()
    print(fully_capitalized)

    # Output line 3: String with first letter of every word capitalized (Title Case)
    title_cased = original_string.title()
    print(title_cased)

if __name__ == '__main__':
    main()