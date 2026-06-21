def evaluate_nested_logic(a, b, c):
    result = not (a and (b or not c))
    return result

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    
    result = evaluate_nested_logic(sample_a, sample_b, sample_c)
    print(result)