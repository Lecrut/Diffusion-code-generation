def repeat_sequence(sequence, n):
    return sequence * n
if __name__ == '__main__':
    pattern = 'AB'
    repetitions = 1000
    result = repeat_sequence(pattern, repetitions)
    print(result[:20])