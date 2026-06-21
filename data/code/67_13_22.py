def find_pair_with_sum(numbers, target):
    num_set = set()
    for number in numbers:
        complement = target - number
        if complement in num_set:
            return (complement, number)
        num_set.add(number)
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    sample_numbers = [2, 7, 11, 15]
    target_sum = 9
    try:
        result = find_pair_with_sum(sample_numbers, target_sum)
        print(result)
    except ValueError as e:
        print(e)