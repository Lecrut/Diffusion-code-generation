def compare_lengths(length_a, length_b):
    difference = abs(length_a - length_b)
    if length_a > length_b:
        return f'Length A is longer than Length B by {difference} units'
    elif length_a < length_b:
        return f'Length B is longer than Length A by {difference} units'
    else:
        return 'Both lengths are equal'

if __name__ == '__main__':
    length_a = 15
    length_b = 10
    print(compare_lengths(length_a, length_b))