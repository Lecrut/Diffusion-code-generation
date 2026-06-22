import collections

def run_length_encode(text):
    if not text:
        return {}
    
    counts = collections.Counter(text)
    return dict(counts)

if __name__ == '__main__':
    sample_texts = [
        "aabcccccaaa",
        "abcabc",
        "",
        "a",
        "aaaabbbccd"
    ]
    
    results = {}
    for text in sample_texts:
        encoded = run_length_encode(text)
        results[text] = encoded
        print(encoded)