def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings.")
    return f"{str1}{str2}"

if __name__ == '__main__':
    GREETING_PART1 = "Hello"
    GREETING_PART2 = "World!"
    LANGUAGE_PART1 = "Python"
    LANGUAGE_PART2 = "Programming"

    greeting_result = combine_strings(GREETING_PART1, GREETING_PART2)
    language_result = combine_strings(LANGUAGE_PART1, LANGUAGE_PART2)

    print(f"Greeting Combined: {greeting_result}")
    print(f"Language Combined: {language_result}")