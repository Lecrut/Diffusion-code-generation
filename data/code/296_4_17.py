def find_pairs_with_ratio(numbers, target_ratio):
    if not numbers or len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    num_to_index = {}
    pairs = []
    
    for i, num in enumerate(numbers):
        if num == 0 and target_ratio != 0:
            continue
        
        required_num = num * target_ratio
        if required_num in num_to_index:
            pairs.append((num_to_index[required_num], i))
        
        num_to_index[num] = i
    
    return pairs

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    target_ratio = 2
    result = find_pairs_with_ratio(sample_numbers, target_ratio)
    print(f"Pairs with ratio {target_ratio}: {result}")