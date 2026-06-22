import re

def split_preserving_quotes(input_string):
    pattern = r'(?:"(?:[^"]*")|(?:[^",]+))+'
    matches = re.findall(pattern, input_string)
    cleaned_tokens = [match.strip() for match in matches if match.strip()]
    return cleaned_tokens

if __name__ == '__main__':
    sample_input = 'simple,"quoted, value",another "one, two",end'
    result = split_preserving_quotes(sample_input)
    print(result)