def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def convert_string(text):
    validate_input(text)
    lowercase_text = text.lower()
    uppercase_text = text.upper()
    titlecase_text = text.title()
    return lowercase_text, uppercase_text, titlecase_text

if __name__ == '__main__':
    sample_string = "Example String for Conversion"
    lower, upper, title = convert_string(sample_string)
    print("Original:", sample_string)
    print("Lowercase:", lower)
    print("Uppercase:", upper)
    print("Title Case:", title)