def check_at_least_one(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample_values = [
        [False, False, False],
        [True, False, False],
        [],
        [0, False, None],
        [1, 0, False]
    ]
    
    for values in sample_values:
        print(f"Input: {values}, Output: {check_at_least_one(values)}")