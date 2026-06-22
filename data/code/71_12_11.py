def get_middle(lst):
    if not lst:
        raise ValueError("List must not be empty")
    
    count = len(lst)
    half = count // 2
    is_odd = count % 2 == 1
    
    if is_odd:
        return lst[half]
    
    left_val = lst[half - 1]
    right_val = lst[half]
    return (left_val + right_val) / 2

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50, 60, 70]
    sample_even = [100, 200, 300, 400]
    
    result_odd = get_middle(sample_odd)
    result_even = get_middle(sample_even)
    
    print(result_odd)
    print(result_even)