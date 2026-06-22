SUM_HEADER = "The total of {sequence} is: {total}"

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list1 = [1, 5, 10, 2]
    sample_list2 = [-1, 2, -3, 4, 5]

    result1 = calculate_sum(sample_list1)
    print(SUM_HEADER.format(sequence=sample_list1, total=result1))

    result2 = calculate_sum(sample_list2)
    print(SUM_HEADER.format(sequence=sample_list2, total=result2))