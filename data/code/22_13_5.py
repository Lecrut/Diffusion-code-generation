num_is_odd = num % 2 != 0 if 'num' in locals() else None

if __name__ == '__main__':
    test_cases = [5, -3, 4, -1]
    for n in test_cases:
        local_num = n
        result = (local_num % 2 != 0)
        print(f"num={n}, is_odd={result}")