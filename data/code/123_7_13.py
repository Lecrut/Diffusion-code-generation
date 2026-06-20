def sum_even_numbers(start, end):
    return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    start_value = 3
    end_value = 25
    result = sum_even_numbers(start_value, end_value)
    print(result)