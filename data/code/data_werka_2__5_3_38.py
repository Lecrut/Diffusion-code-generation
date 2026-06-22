def validate_length(length):
    if not isinstance(length, (int, float)):
        raise ValueError("Length must be an integer or float.")
    if length < 0:
        raise ValueError("Length cannot be negative.")

def compare_lengths(length_a, length_b):
    validate_length(length_a)
    validate_length(length_b)
    
    difference = abs(length_a - length_b)
    if length_a > length_b:
        return f"Length A is longer than Length B by {difference} units"
    elif length_b > length_a:
        return f"Length B is longer than Length A by {difference} units"
    else:
        return "Both lengths are equal"

if __name__ == '__main__':
    length_a = 20
    length_b = 15
    result = compare_lengths(length_a, length_b)
    print(result)