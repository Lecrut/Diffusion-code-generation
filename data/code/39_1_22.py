import re

def extract_non_overlapping(text, pattern):
    matches = re.findall(pattern, text)
    return matches

if __name__ == '__main__':
    input_string = "hello world hello universe hello galaxy"
    search_pattern = r"\bhello\b"
    
    found_occurrences = extract_non_overlapping(input_string, search_pattern)
    print(found_occurrences)