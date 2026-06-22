def extract_first(input_list):
    return input_list[:1][0]

if __name__ == '__main__':
    data = [1, "hello", 3.14, None]
    result = extract_first(data)
    print(result)