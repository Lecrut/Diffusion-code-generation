import re

def remove_duplicate_punctuation(text):
    punctuation = r'[!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~]'
    pattern = f'({punctuation})'
    result = []
    seen = set()
    
    for match in re.finditer(pattern, text):
        if match.group(1) not in seen:
            seen.add(match.group(1))
            result.append(match.group(0))
    
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Isn't it fun? Yes, it is!"
    print(remove_duplicate_punctuation(sample_text))