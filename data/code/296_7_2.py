def manipulate_ratio(a, b):
    initial_ratio = (a, b)
    print(f"Initial ratio a:b is {a}:{b}")
    new_a_half = a / 2
    print(f"Ratio after halving a:b is {new_a_half}:{b}")
    new_b_double = b * 2
    print(f"Ratio after doubling b:b is {a}:{new_b_double}")
    inverted_ratio = (b, a)
    print(f"Ratio after inverting a:b is {inverted_ratio[0]}:{inverted_ratio[1]}")
if __name__ == '__main__':
    a_val = 10
    b_val = 4
    manipulate_ratio(a_val, b_val)