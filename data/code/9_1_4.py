def clean_strings(input_list):
    return [s.strip() for s in input_list]

if __name__ == '__main__':
    sample_data = [
        "  hello world  ",
        "\t\nPython Code\t\n",
        "   ",
        "  No extra spaces   ",
        "  \t  mixed   \t  whitespace  \n  "
    ]
    cleaned_result = clean_strings(sample_data)
    print(cleaned_result)