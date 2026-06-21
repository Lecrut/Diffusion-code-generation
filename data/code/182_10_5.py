def insert_delimiter(input_string, delimiter):
    return delimiter.join(input_string)

if __name__ == '__main__':
    result = insert_delimiter("hello", "-")
    print(result)