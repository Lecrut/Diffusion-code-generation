def replace_spaces_with_underscores(text):
    return text.replace(" ", "_")

if __name__ == "__main__":
    sample_string = "Hello World Python Programming"
    result = replace_spaces_with_underscores(sample_string)
    print(result)