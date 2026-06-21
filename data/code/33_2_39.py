SPACE_CHARACTER = ' '

def remove_spaces(s):
    return ''.join([char for char in s if char != SPACE_CHARACTER])

if __name__ == '__main__':
    sample_string = "Hello World from Alibaba Cloud"
    result = remove_spaces(sample_string)
    print(result)