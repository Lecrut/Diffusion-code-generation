def compare_lengths(length_a, length_b):
    difference = abs(length_a - length_b)
    if length_a > length_b:
        result = f"Length A is longer than Length B by {difference} units"
    elif length_b > length_a:
        result = f"Length B is longer than Length A by {difference} units"
    else:
        result = "Length A is equal to Length B"
    return result

if __name__ == '__main__':
    length_a = 10.5
    length_b = 7.2
    print(compare_lengths(length_a, length_b))