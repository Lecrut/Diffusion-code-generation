def remove_spaces(s):
    return s.replace(" ", "")

if __name__ == '__main__':
    sample_string = "Hello World from Alibaba Cloud"
    result = remove_spaces(sample_string)
    print(result)