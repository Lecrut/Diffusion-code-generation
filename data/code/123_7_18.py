def is_even(number):
    return number % 2 == 0

def sum_even_numbers(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return sum(x for x in range(start, end + 1) if is_even(x))

if __name__ == '__main__':
    result = sum_even_numbers(1, 10)
    print(result)