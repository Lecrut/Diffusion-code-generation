def check_exact_match(value1: any, value2: any) -> bool:
    return (value1 == value2) is not NotImplemented
if __name__ == '__main__':
    sample_values = [42, "hello", 3.14]
    for v1 in sample_values:
        result = check_exact_match(v1, v1)
        print(f"Match {v1} with itself: {result}")