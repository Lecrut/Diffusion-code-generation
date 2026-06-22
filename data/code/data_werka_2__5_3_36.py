def compare_lengths(length_a, length_b):
    if length_a == length_b:
        return "Length A and Length B are equal"
    
    difference = abs(length_a - length_b)
    longer_length = "A" if length_a > length_b else "B"
    
    return f"Length {longer_length} is longer than Length {'B' if longer_length == 'A' else 'A'} by {difference} units"

if __name__ == '__main__':
    length_a = 20
    length_b = 15
    result = compare_lengths(length_a, length_b)
    print(result)