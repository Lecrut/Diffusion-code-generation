REVERSE_SLICE = -1

reverse_string = lambda s: s[::REVERSE_SLICE]

if __name__ == '__main__':
    SAMPLE_INPUT = "Alibaba Cloud"
    print(reverse_string(SAMPLE_INPUT))