def repeat_sequence(sequence, n):
    if n <= 0:
        return []
    return sequence * n
if __name__ == '__main__':
    sequence = [1, 2, 3]
    n = 5
    result = repeat_sequence(sequence, n)
    print(result)