THRESHOLD = 0

def compare_values(a, b):
    return a > b + THRESHOLD

if __name__ == '__main__':
    SAMPLE_VALUE1 = 42
    SAMPLE_VALUE2 = 27
    result = compare_values(SAMPLE_VALUE1, SAMPLE_VALUE2)
    print(result)