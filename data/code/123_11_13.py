NUMBERS = [1, 5, 10, 2, 8]

def calculate_cumulative_sum(numbers):
    cumulative_sums = []
    total_sum = 0
    for number in numbers:
        total_sum += number
        cumulative_sums.append(total_sum)
    return cumulative_sums

if __name__ == '__main__':
    result = calculate_cumulative_sum(NUMBERS)
    print(result)