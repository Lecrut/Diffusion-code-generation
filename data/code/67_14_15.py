def find_pair_with_sum(numbers, target):
    num_set = set()
    for number in numbers:
        complement = target - number
        if complement in num_set:
            return (complement, number)
        num_set.add(number)
    raise ValueError("No two distinct elements add up to the target value.")

if __name__ == '__main__':
    sample_numbers = [2, 7, 11, 15]
    target_value = 9
    try:
        result = find_pair_with_sum(sample_numbers, target_value)
        print(result)
    except ValueError as e:
        print(e)