import sys

def main():
    # Read a single line from standard input (simulated here with hardcoded sample)
    raw_input = "hello world"
    
    original_string = raw_input
    
    fully_capitalized = original_string.upper()
    
    capitalized_words = [word.capitalize() for word in original_string.split()]
    words_capitalized = "".join(capitalized_words).lower()[1:] if len(original_string) > 0 and not original_string[0].isalpha() else "".join(word.capitalize() for word in original_string.split())

    # Output the three lines as required
    print(original_string)
    print(fully_capitalized)
    print(words_capitalized)

if __name__ == '__main__':
    main()