length_a = 150
length_b = 120

def compare_lengths(a, b):
    if a > b:
        return f"Length A is longer than Length B by {a - b} units"
    elif a < b:
        return f"Length A is shorter than Length B by {b - a} units"
    else:
        return "Length A is equal to Length B"

if __name__ == '__main__':
    result = compare_lengths(length_a, length_b)
    print(result)