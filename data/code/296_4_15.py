def find_pairs_with_ratio(numbers, target_ratio):
    num_set = set()
    pairs = []
    for number in numbers:
        if number != 0:
            reciprocal = number / target_ratio
            if reciprocal in num_set:
                pairs.append((reciprocal, number))
            num_set.add(number)
    return pairs

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    target_ratio = 0.5
    print(find_pairs_with_ratio(sample_numbers, target_ratio))