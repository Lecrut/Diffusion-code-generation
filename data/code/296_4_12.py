def find_pairs_with_ratio(numbers, target_ratio):
    num_set = set()
    pairs = []
    
    for number in numbers:
        if number == 0 and target_ratio == 0:
            continue
        if number != 0 and (number * target_ratio) in num_set:
            pairs.append((int(number), int(number * target_ratio)))
        num_set.add(number)
    
    return pairs

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 8, 10]
    sample_target_ratio = 2
    result = find_pairs_with_ratio(sample_numbers, sample_target_ratio)
    print(result)