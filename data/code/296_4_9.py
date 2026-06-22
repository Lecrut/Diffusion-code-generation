def find_pairs_with_ratio(numbers, target_ratio):
    seen = set()
    pairs = []
    for number in numbers:
        if number == 0 and target_ratio == 0:
            continue
        if number != 0 and number * target_ratio in seen:
            pairs.append((number * target_ratio, number))
        seen.add(number)
    return pairs

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    sample_target_ratio = 0.5
    print(find_pairs_with_ratio(sample_numbers, sample_target_ratio))