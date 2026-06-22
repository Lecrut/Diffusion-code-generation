def has_no_special_characters(text):
    result = True
    for char in text:
        if not char.isalnum():
            result = False
            break
    return result

if __name__ == '__main__':
    sample_string = "HelloWorld123"
    print(has_no_special_characters(sample_string))