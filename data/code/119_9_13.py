def reverse_integers(a, b):
    a, b = b, a
    return a, b

if __name__ == '__main__':
    original_a = 15
    original_b = 25
    reversed_a, reversed_b = reverse_integers(original_a, original_b)
    print(f"Before reversal: a={original_a}, b={original_b}")
    print(f"After reversal: a={reversed_a}, b={reversed_b}")