TOTAL = 0

def calculate_sum(numbers):
    global TOTAL
    for number in numbers:
        TOTAL += number
    return TOTAL

if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    result = calculate_sum(sample_list)
    print(result)