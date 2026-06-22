def segment_phrase(phrase, delimiters):
    return [segment for segment in phrase.split() if segment not in delimiters]

if __name__ == '__main__':
    SAMPLE_PHRASE = "apple,banana;orange,grape"
    DELIMITERS = [',', ';']
    result = segment_phrase(SAMPLE_PHRASE.replace('', ' ').strip(), DELIMITERS)
    print(result)