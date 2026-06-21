reverse_string = lambda s: ''.join([s[i] for i in range(len(s)-1, -1, -1)])
if __name__ == '__main__':
    sample_string = "test"
    print(reverse_string(sample_string))