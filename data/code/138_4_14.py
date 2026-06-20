def bitwise_operations(a, b):
    return [(a and b), (a or b), (a ^ b)]

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    print(bitwise_operations(sample_a, sample_b))