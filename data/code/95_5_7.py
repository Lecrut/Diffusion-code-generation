def analyze_integers(a, b, c):
    lookup = {"first": lambda x: x > 0, "second": lambda x: x % 2 == 0}
    
    if a == 0:
        raise ValueError("First argument must be non-zero for divisibility check")
        
    results = {}
    results["first_positive"] = lookup["first"](a)
    results["second_even"] = lookup["second"](b)
    results["third_divisible"] = c % a == 0
    
    return (results["first_positive"], results["second_even"], results["third_divisible"])

if __name__ == '__main__':
    sample_a = 7
    sample_b = 8
    sample_c = 21
    output = analyze_integers(sample_a, sample_b, sample_c)
    print(output)