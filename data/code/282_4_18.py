TOTAL_FORMAT = "The total of {numbers} is: {total}"

def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    result = calculate_total(sample_list)
    print(TOTAL_FORMAT.format(numbers=sample_list, total=result))