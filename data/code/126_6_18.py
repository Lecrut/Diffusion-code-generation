def compare_integers(x, y):
    return x == y

if __name__ == '__main__':
    value1 = 42
    value2 = 42
    result1 = compare_integers(value1, value2)
    print(f"Checking equality between {value1} and {value2}: {result1}")
    
    value3 = 75
    value4 = 100
    result2 = compare_integers(value3, value4)
    print(f"Checking equality between {value3} and {value4}: {result2}")