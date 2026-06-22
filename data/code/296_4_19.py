def find_pairs_with_ratio(numbers, target_ratio):
    num_set = set()
    pairs = []
    for number in numbers:
        if number == 0 and target_ratio == 0:
            continue
        if number != 0 and target_ratio * number in num_set:
            pairs.append((target_ratio * number, number))
        num_set.add(number)
    return pairs

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    sample_target_ratio = 0.5
    print(find_pairs_with_ratio(sample_numbers, sample_target_ratio))