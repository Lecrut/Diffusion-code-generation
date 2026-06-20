import re

def split_preserving_quotes(text):
    pattern = r'''(?:'[^']*'|"[^"]*"|[^,])+'''
    matches = re.findall(pattern, text)
    return [match.strip() for match in matches]

if __name__ == '__main__':
    sample_input = 'apple, "banana, split", cherry, "date, fig", grape'
    result = split_preserving_quotes(sample_input)
    print(result)