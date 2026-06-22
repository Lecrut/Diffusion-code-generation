def normalize_text(text):
    return text.strip()

if __name__ == '__main__':
    sample_texts = [
        '  hello world  ',
        '   python programming   ',
        'no leading or trailing spaces',
        '   ',
        ''
    ]
    normalized_results = [normalize_text(t) for t in sample_texts]
    for original, normalized in zip(sample_texts, normalized_results):
        print(f"Original: {repr(original)}, Normalized: {repr(normalized)}")