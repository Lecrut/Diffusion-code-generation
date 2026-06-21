NUMBERS = "10 20 30 40"

def sum_numbers(numbers_str):
    numbers = numbers_str.split()
    total_sum = sum(map(int, numbers))
    return total_sum

if __name__ == '__main__':
    result = sum_numbers(NUMBERS)
    print(result)