def lucas_sequence(n):
    if n == 0:
        return [2]
    elif n == 1:
        return [2, 1]
    
    sequence = [2, 1]
    for i in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence

if __name__ == '__main__':
    print(lucas_sequence(9))