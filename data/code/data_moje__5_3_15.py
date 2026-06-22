def compare_lengths(length_a, length_b):
    difference = length_a - length_b
    if length_a > length_b:
        return f"Length A is longer than Length B by {difference} units"
    elif length_a < length_b:
        return f"Length A is shorter than Length B by {abs(difference)} units"
    else:
        return f"Length A is equal to Length B"

if __name__ == '__main__':
    length_a = 15.5
    length_b = 10.2
    result = compare_lengths(length_a, length_b)
    print(result)