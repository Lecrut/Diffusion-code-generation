import re

def custom_delimiter_split(text, delimiters):
    combined_pattern = '|'.join(map(re.escape, delimiters))
    words = re.split(combined_pattern, text)
    return [word.strip() for word in words if word]

if __name__ == '__main__':
    sample_text = "This,is:a,sample,text;with various:delimiters."
    delimiters = [',', ';', ':']
    result = custom_delimiter_split(sample_text, delimiters)
    print(result)