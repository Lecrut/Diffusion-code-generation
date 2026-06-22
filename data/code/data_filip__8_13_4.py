def split_comma_separated(text):
    return (element.strip() for element in text.split(',') if element.strip())

if __name__ == '__main__':
    sample_string = "  apple, banana, , cherry ,  "
    result = list(split_comma_separated(sample_string))
    print(result)