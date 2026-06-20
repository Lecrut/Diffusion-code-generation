def reverse_integers(a, b):
    try:
        a, b = b, a
        return a, b
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    original_a = 10
    original_b = 20
    reversed_values = reverse_integers(original_a, original_b)
    if reversed_values is not None:
        print(f"After reversal: a={reversed_values[0]}, b={reversed_values[1]}")