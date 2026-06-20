def replace_spaces_with_underscores(text):
    return text.replace(" ", "_")

if __name__ == '__main__':
    sample_text = "hello world python"
    result = replace_spaces_with_underscores(sample_text)
    print(result)