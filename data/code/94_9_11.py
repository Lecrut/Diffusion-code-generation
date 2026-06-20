def check_at_least_one(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample1 = [False, False, True]
    sample2 = []
    sample3 = [False, 0, None, ""]
    
    print(f"Sample 1: {sample1} -> {check_at_least_one(sample1)}")
    print(f"Sample 2: {sample2} -> {check_at_least_one(sample2)}")
    print(f"Sample 3: {sample3} -> {check_at_least_one(sample3)}")