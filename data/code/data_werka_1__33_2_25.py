def remove_spaces(s):
    return ''.join(s.split())

if __name__ == '__main__':
    sample_string = "Hello World from Qwen"
    result = remove_spaces(sample_string)
    print(result)