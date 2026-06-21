def extract_odd_numbers(start, end):
    return [num for num in range(start, end + 1) if num % 2 != 0]

if __name__ == '__main__':
    start_value = 15
    end_value = 30
    odd_nums = extract_odd_numbers(start_value, end_value)
    print(odd_nums)