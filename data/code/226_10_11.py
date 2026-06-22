REPEAT_COUNT = 3

def repeat_sequence(sequence, count):
    return sequence * count

if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    result = repeat_sequence(sample_sequence, REPEAT_COUNT)
    print(result)