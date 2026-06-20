def sum_even_numbers(start, end):
    return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    result = sum_even_numbers(3, 20)
    print(result)