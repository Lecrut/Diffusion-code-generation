AND = lambda x, y: x & y
OR = lambda x, y: x | y
NOT = lambda x: ~x

if __name__ == '__main__':
    sample_a = 5
    sample_b = 3
    
    and_result = AND(sample_a, sample_b)
    or_result = OR(sample_a, sample_b)
    not_a_result = NOT(sample_a)
    not_b_result = NOT(sample_b)
    
    print(f"A: {sample_a} ({bin(sample_a)})")
    print(f"B: {sample_b} ({bin(sample_b)})")
    print(f"A AND B: {and_result} ({bin(and_result)})")
    print(f"A OR B: {or_result} ({bin(or_result)})")
    print(f"NOT A: {not_a_result} ({bin(not_a_result)})")
    print(f"NOT B: {not_b_result} ({bin(not_b_result)})")