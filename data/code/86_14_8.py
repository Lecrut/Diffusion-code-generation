def bitwise_logical_equivalence(a: bool, b: bool) -> bool:
    return (a & b) | (~a & ~b)

if __name__ == '__main__':
    sample1 = bitwise_logical_equivalence(True, True)
    print(sample1)
    
    sample2 = bitwise_logical_equivalence(False, False)
    print(sample2)
    
    sample3 = bitwise_logical_equivalence(True, False)
    print(sample3)