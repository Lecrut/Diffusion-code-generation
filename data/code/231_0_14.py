if __name__ == '__main__':
    pattern_length = 20
    repeating_sequence = 'AB'
    repeated_pattern = ''.join([repeating_sequence for _ in range(pattern_length // len(repeating_sequence))])
    if len(repeated_pattern) < pattern_length:
        repeated_pattern += repeating_sequence[:pattern_length - len(repeated_pattern)]
    print(repeated_pattern)