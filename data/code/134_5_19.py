def check_single_activation(a, b):
    return (a and not b) or (not a and b)

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    print(f"Check with sample values: {check_single_activation(sample_a, sample_b)}")