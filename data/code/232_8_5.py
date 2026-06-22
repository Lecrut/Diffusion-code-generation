def growing_sequence(start, end):
    sequence = []
    for i in range(start, end + 1):
        sequence.append(i)
    return sequence

if __name__ == '__main__':
    result = growing_sequence(1, 5)
    print(result)