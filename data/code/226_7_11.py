sample_values = [True, False, True, False] * 25

if __name__ == '__main__':
    result = sample_values[:]
    for _ in range(9):
        result += sample_values
    print(result)