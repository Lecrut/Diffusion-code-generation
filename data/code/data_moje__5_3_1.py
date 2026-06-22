def compare_lengths(length_a, length_b):
    difference = length_a - length_b
    if difference > 0:
        return f"Length A is longer than Length B by {difference} units"
    elif difference < 0:
        return f"Length B is longer than Length A by {abs(difference)} units"
    else:
        return f"Length A and Length B are equal"

if __name__ == '__main__':
    length_a = 10.5
    length_b = 5.2
    result = compare_lengths(length_a, length_b)
    print(result)