def repeat_sequence(sequence, n):
    return sequence * n

if __name__ == '__main__':
    SEQUENCE = 'AB'
    REPETITIONS = 1000
    
    result = repeat_sequence(SEQUENCE, REPETITIONS)
    print(result)