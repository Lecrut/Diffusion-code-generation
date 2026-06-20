def sum_even_numbers(start, end):
    return sum(num for num in range(start, end + 1) if num % 2 == 0)

if __name__ == '__main__':
    result = sum_even_numbers(5, 15)
    print(result)