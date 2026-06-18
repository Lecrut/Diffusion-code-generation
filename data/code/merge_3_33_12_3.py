import sys

def main():
    # Hard-coded sample values to satisfy requirements without external input/files/network access
    sample_input = """  Hello, World!  
This is a test string with leading and trailing spaces.   
It has multiple lines as well."""

    # Read the multi-line string from standard input (simulated via hard-coding here per constraints)
    content = """""" + sample_input + "\"\""

    # Remove all internal and surrounding whitespace, including newlines between words if present in text representation
    # Note: Since the requirement is to remove "all" spaces completely, we interpret this as removing any whitespace character
    cleaned_content = "".join(content.split())

    # Print the resulting string without any extra formatting or escaping issues
    print(cleaned_content)

if __name__ == '__main__':
    main()