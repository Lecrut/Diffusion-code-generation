def compare_lengths(length_a, length_b):
    difference = abs(length_a - length_b)
    if length_a > length_b:
        return f'Length A is longer than Length B by {difference} units'
    elif length_a < length_b:
        return f'Length B is longer than Length A by {difference} units'
    else:
        return 'Length A and Length B are equal'

if __name__ == '__main__':
    length_a = 10
    length_b = 5
    result = compare_lengths(length_a, length_b)
    print(result)