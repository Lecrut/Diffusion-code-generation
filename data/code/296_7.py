def manipulate_ratio(a, b):
    initial_ratio = (a, b)
    print(f"Initial ratio a:b is {a}:{b}")
    new_a_half = a // 2
    new_b_half = b // 2
    print(f"Ratio after halving (a/2):(b/2) is {new_a_half}:{new_b_half}")
    new_a_double = a * 2
    new_b_double = b * 2
    print(f"Ratio after doubling (2a):(2b) is {new_a_double}:{new_b_double}")
    new_a_inv = b
    new_b_inv = a
    print(f"Ratio after inverting (b):(a) is {new_a_inv}:{new_b_inv}")
if __name__ == '__main__':
    a_val = 10
    b_val = 4
    manipulate_ratio(a_val, b_val)