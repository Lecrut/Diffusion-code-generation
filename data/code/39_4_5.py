def segment_phrase(phrase, delimiters):
    segments = []
    current_segment = ""
    for char in phrase:
        if char in delimiters:
            if current_segment:
                segments.append(current_segment)
            current_segment = ""
        else:
            current_segment += char
    if current_segment:
        segments.append(current_segment)
    return segments
if __name__ == '__main__':
    phrase1 = "apple,banana,orange;grape"
    delimiters1 = [',', ';']
    result1 = segment_phrase(phrase1, delimiters1)
    print(f"Phrase: {phrase1}, Delimiters: {delimiters1}")
    print(f"Result: {result1}")
    phrase2 = "one|two-three/four"
    delimiters2 = ['|', '-', '/']
    result2 = segment_phrase(phrase2, delimiters2)
    print(f"Phrase: {phrase2}, Delimiters: {delimiters2}")
    print(f"Result: {result2}")
    phrase3 = "a b c d"
    delimiters3 = [' ']
    result3 = segment_phrase(phrase3, delimiters3)
    print(f"Phrase: {phrase3}, Delimiters: {delimiters3}")
    print(f"Result: {result3}")
    phrase4 = "startend"
    delimiters4 = ['a', 'b']
    result4 = segment_phrase(phrase4, delimiters4)
    print(f"Phrase: {phrase4}, Delimiters: {delimiters4}")
    print(f"Result: {result4}")