def replace_spaces_with_underscores(text):
    return text.replace(" ", "_")

if __name__ == "__main__":
    test_input = "hello world example"
    result = replace_spaces_with_underscores(test_input)
    print(result)