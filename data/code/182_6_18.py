def ord_map(input_string):
    return list(map(ord, input_string))

if __name__ == '__main__':
    sample_string = "Hello World"
    result = ord_map(sample_string)
    print(result)