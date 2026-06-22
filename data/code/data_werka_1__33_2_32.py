SPACE_REMOVER = lambda s: ''.join(s.split())

if __name__ == '__main__':
    SAMPLE_STRING = "This is a test string with spaces."
    RESULT = SPACE_REMOVER(SAMPLE_STRING)
    print(RESULT)