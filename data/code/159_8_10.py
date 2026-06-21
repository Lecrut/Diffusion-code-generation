def collect_odd_numbers(dataset):
    odd_numbers = []
    for number in dataset:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers

def validate_dataset(dataset):
    if not isinstance(dataset, list) or len(dataset) == 0:
        return False
    for item in dataset:
        if not isinstance(item, int):
            return False
    return True
if __name__ == '__main__':
    sample_dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if validate_dataset(sample_dataset):
        odd_numbers = collect_odd_numbers(sample_dataset)
        print(odd_numbers)
    else:
        print('Invalid dataset provided.')