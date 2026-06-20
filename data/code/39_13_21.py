def extract_substrings(text, start_marker, end_marker):
    results = []
    start = 0
    while True:
        start_idx = text.find(start_marker, start)
        if start_idx == -1:
            break
        start_idx += len(start_marker)
        end_idx = text.find(end_marker, start_idx)
        if end_idx == -1:
            break
        results.append(text[start_idx:end_idx])
        start = end_idx + len(end_marker)
    return results

if __name__ == '__main__':
    sample_text = "hello [world] foo [bar] baz [qux]"
    start = '['
    end = ']'
    print(extract_substrings(sample_text, start, end))