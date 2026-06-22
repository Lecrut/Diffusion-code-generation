def validate_length(value):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Length must be a non-negative number")

def compare_lengths(length1, length2):
    validate_length(length1)
    validate_length(length2)
    
    if length1 > length2:
        return length1
    elif length2 > length1:
        return length2
    else:
        return None

if __name__ == '__main__':
    length_a = 5.0
    length_b = 3.0
    longer_length = compare_lengths(length_a, length_b)
    print(f"The longer length is: {longer_length}")
    
    length_c = 2.5
    length_d = 2.5
    same_length = compare_lengths(length_c, length_d)
    print(f"Are the lengths the same? {'Yes' if same_length is None else 'No'}")