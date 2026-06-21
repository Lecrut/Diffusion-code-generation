REVERSE_STEP = -1

reverse_string = lambda s: s[::REVERSE_STEP]

if __name__ == '__main__':
    SAMPLE_INPUT = "Alibaba Cloud"
    print(reverse_string(SAMPLE_INPUT))