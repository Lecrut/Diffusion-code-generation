def find_pairs_with_ratio(numbers, target_ratio):
    num_dict = {}
    pairs = []
    for number in numbers:
        if number != 0 and (number * target_ratio) in num_dict:
            pairs.append((int(number * target_ratio), number))
        num_dict[number] = True
    return pairs

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    target_ratio = 2
    result = find_pairs_with_ratio(sample_numbers, target_ratio)
    print(result)