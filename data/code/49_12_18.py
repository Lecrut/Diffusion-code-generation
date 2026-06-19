EPSILON = 1e-09

def compare_lengths(length1, length2):
    if abs(length1 - length2) < EPSILON:
        return None
    elif length1 > length2:
        return length1
    else:
        return length2
if __name__ == '__main__':
    l1 = 10.00000001
    l2 = 10.0
    result = compare_lengths(l1, l2)
    print(f'The greater length is: {result}')
    l3 = 5.0
    l4 = 7.5
    result = compare_lengths(l3, l4)
    print(f'The greater length is: {result}')
    l5 = 12.3456789
    l6 = 12.3456788
    result = compare_lengths(l5, l6)
    print(f'The greater length is: {result}')