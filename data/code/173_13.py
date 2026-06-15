def group_multiples_of_three(data):
    multiples_of_three = []
    not_multiples_of_three = []
    for number in data:
        if number % 3 == 0:
            multiples_of_three.append(number)
        else:
            not_multiples_of_three.append(number)
    return multiples_of_three, not_multiples_of_three
if __name__ == '__main__':
    sample_data = list(range(1, 100))
    multiples, non_multiples = group_multiples_of_three(sample_data)
    print(f"Multiples of 3: {multiples}")
    print(f"Not Multiples of 3: {non_multiples}")