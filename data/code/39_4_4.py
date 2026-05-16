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
    test_phrase = "apple,banana;orange,grape"
    test_delimiters = [',', ';']
    result = segment_phrase(test_phrase, test_delimiters)
    print(result)
    test_phrase_2 = "one|two-three/four"
    test_delimiters_2 = ['|', '-', '/']
    result_2 = segment_phrase(test_phrase_2, test_delimiters_2)
    print(result_2)
    test_phrase_3 = "a b c d"
    test_delimiters_3 = [' ']
    result_3 = segment_phrase(test_phrase_3, test_delimiters_3)
    print(result_3)