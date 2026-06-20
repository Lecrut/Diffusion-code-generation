import re

def split_and_clean(input_string):
    return [part.strip() for part in re.split(r',', input_string) if part.strip()]

if __name__ == '__main__':
    sample_input = " apple, banana, , cherry , ,date "
    result = split_and_clean(sample_input)
    print(result)