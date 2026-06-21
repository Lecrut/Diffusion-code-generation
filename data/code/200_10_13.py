IS_ALPHA = str.isalpha

def filter_alphabetic(strings):
    return [s for s in strings if IS_ALPHA(s)]
if __name__ == '__main__':
    sample_values = ['hello', 'world!', 'Python3', 'code']
    filtered_list = filter_alphabetic(sample_values)
    print(filtered_list)