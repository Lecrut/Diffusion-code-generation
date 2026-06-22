def find_opposite_truth(truth: bool) -> bool:
    return not truth

def main():
    test_val1 = True
    test_val2 = False
    result1 = find_opposite_truth(test_val1)
    result2 = find_opposite_truth(test_val2)
    print(result1)
    print(result2)

if __name__ == '__main__':
    main()