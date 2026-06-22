def capitalize_first_letter(s):
    if not s:
        return s
    first_char = s[0]
    if first_char.islower():
        return first_char.upper() + s[1:]
    return s

if __name__ == '__main__':
    print(capitalize_first_letter('hello'))
    print(capitalize_first_letter(''))
    print(capitalize_first_letter('a'))
    print(capitalize_first_letter('Äpfel'))
    print(capitalize_first_letter(' already capitalized'))
    print(capitalize_first_letter('123abc'))