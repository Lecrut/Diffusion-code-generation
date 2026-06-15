import re
def process_text(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    filtered_tokens = [token for token in tokens if len(token) >= 3]
    return filtered_tokens
if __name__ == '__main__':
    sample_text = "This is a large block of text that needs to be processed efficiently. Short words like 'a', 'is', and 'of' should be removed. We need more than three characters."
    result = process_text(sample_text)
    print(result)