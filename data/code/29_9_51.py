REVERSE_STEP = -1

reverse_string = lambda s: s[::REVERSE_STEP]

if __name__ == '__main__':
    SAMPLE_STRING = "test"
    print(reverse_string(SAMPLE_STRING))