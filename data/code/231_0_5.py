if __name__ == '__main__':
    pattern_length = 20
    repeating_pattern = 'AB'
    result = ''.join([repeating_pattern for _ in range(pattern_length // len(repeating_pattern))])
    print(result)