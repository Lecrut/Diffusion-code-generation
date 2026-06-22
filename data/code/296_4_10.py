def find_pairs_with_ratio(numbers, target_ratio):
    num_dict = {}
    pairs = set()
    
    for number in numbers:
        if number == 0 and target_ratio == 0:
            continue
        if number != 0:
            inverse = number / target_ratio
            if inverse in num_dict:
                pairs.add((inverse, number))
        if number * target_ratio in num_dict:
            pairs.add((number, number * target_ratio))
        
        num_dict[number] = True
    
    return list(pairs)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    sample_target_ratio = 2
    print(find_pairs_with_ratio(sample_numbers, sample_target_ratio))