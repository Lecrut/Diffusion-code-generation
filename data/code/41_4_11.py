def main():
    # Hard-coded sample values to avoid any user input requirements
    original_string = "hello world this is a test string"
    
    # Output 1: The original string
    print(original_string)
    
    # Output 2: Fully capitalized string
    fully_capitalized = original_string.upper()
    print(fully_capitalized)
    
    # Output 3: String with first letter of every word capitalized (Title Case)
    title_case = original_string.title()
    print(title_case)

if __name__ == '__main__':
    main()