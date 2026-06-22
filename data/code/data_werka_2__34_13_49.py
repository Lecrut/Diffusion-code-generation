def capitalize_first_letter(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s.capitalize()

if __name__ == '__main__':
    sample_string = "greetings earthling"
    capitalized_string = capitalize_first_letter(sample_string)
    print(capitalized_string)