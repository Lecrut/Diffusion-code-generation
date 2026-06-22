def repeat_sequence(sequence, n):
    if not isinstance(sequence, str) or not sequence:
        raise ValueError("Invalid sequence")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Invalid repetitions count")
    
    return sequence * n

if __name__ == '__main__':
    pattern = 'AB'
    repetitions = 1000
    result = repeat_sequence(pattern, repetitions)
    print(result)