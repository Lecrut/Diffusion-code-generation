sample_string = "   This is a sample string with  multiple spaces.    "

def split_string(input_str):
    return input_str.split()

if __name__ == '__main__':
    result = split_string(sample_string)
    print(result)