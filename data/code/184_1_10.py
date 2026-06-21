import re

def find_word_boundary(text, pattern):
    compiled_pattern = re.compile(r'\b' + re.escape(pattern) + r'\b')
    return bool(compiled_pattern.search(text))

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    sample_patterns = ["quick", "lazy", "rabbit"]
    
    for pattern in sample_patterns:
        print(f"Pattern '{pattern}' found: {find_word_boundary(sample_text, pattern)}")