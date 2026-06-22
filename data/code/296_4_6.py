def find_pairs_with_ratio(numbers, target_ratio):
    num_dict = {}
    pairs = []
    
    for number in numbers:
        if number == 0 and target_ratio == 0:
            continue
        if number != 0 and target_ratio * number in num_dict:
            pairs.append((target_ratio * number, number))
        num_dict[number] = True
    
    return pairs

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    sample_target_ratio = 0.5
    result = find_pairs_with_ratio(sample_numbers, sample_target_ratio)
    print(result)