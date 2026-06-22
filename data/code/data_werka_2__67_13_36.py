def find_pair_with_sum(numbers, target):
    seen = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return (complement, number)
        seen.add(number)
    raise ValueError("No pair found that adds up to the target sum.")

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    target_sum = 9
    try:
        result = find_pair_with_sum(sample_numbers, target_sum)
        print(result)
    except ValueError as e:
        print(e)