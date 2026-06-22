MAX_REPETITIONS = 10

def repeat_strings(strings, M):
    return [s * M for s in strings if M <= MAX_REPETITIONS]

if __name__ == '__main__':
    sample_strings = ["hello", "world"]
    M = 3
    result = repeat_strings(sample_strings, M)
    print(result)