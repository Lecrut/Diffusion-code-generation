def compare_integers(quantity1, quantity2):
    return quantity1 > quantity2

if __name__ == '__main__':
    sample_quantity1 = 42
    sample_quantity2 = 24
    result = compare_integers(sample_quantity1, sample_quantity2)
    print(f"Comparing {sample_quantity1} and {sample_quantity2}: {result}")