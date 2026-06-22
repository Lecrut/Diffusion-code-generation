def find_pairs_with_ratio(numbers, target_ratio):
    num_set = set()
    pairs = set()

    for number in numbers:
        if number != 0:
            required_number = number * target_ratio
            if required_number in num_set:
                pairs.add((min(number, required_number), max(number, required_number)))
            num_set.add(number)

    return list(pairs)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    target_ratio = 2
    print(find_pairs_with_ratio(sample_numbers, target_ratio))