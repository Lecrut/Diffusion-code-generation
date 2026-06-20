def contains_special_chars(text):
    for char in text:
        if not char.isalnum() and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    sample_strings = ["HelloWorld", "Test@123", "NoSpecialsHere", "Space Only   ", "Mixed#Chars&!"]
    for s in sample_strings:
        result = contains_special_chars(s)
        print(f"{s}: {result}")