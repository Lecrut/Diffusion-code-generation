def xor(a: bool, b: bool) -> bool:
    return (a + b) % 2 == 1

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    print(f"xor({sample_a}, {sample_b}) = {xor(sample_a, sample_b)}")
    
    sample_a = False
    sample_b = True
    print(f"xor({sample_a}, {sample_b}) = {xor(sample_a, sample_b)}")
    
    sample_a = True
    sample_b = True
    print(f"xor({sample_a}, {sample_b}) = {xor(sample_a, sample_b)}")
    
    sample_a = False
    sample_b = False
    print(f"xor({sample_a}, {sample_b}) = {xor(sample_a, sample_b)}")