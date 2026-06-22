def capitalize_first_letter(s):
    if not s:
        return ""
    first_char = s[0].upper()
    rest_of_string = s[1:]
    return first_char + rest_of_string

if __name__ == '__main__':
    sample_values = [
        "the quick brown fox",
        "JUMPS OVER THE LAZY DOG",
        "pYTHON is FUN!",
        "12345 six seven eight",
        "",
        "singleLetter",
        "!@#$%^&*()",
        "aBcDeFgHiJ"
    ]
    for value in sample_values:
        print(capitalize_first_letter(value))