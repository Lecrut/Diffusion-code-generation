EVEN_NUMBER_THRESHOLD = 2

def sum_even_numbers(start, end):
    return sum(x for x in range(start, end + 1) if x % EVEN_NUMBER_THRESHOLD == 0)

if __name__ == '__main__':
    print(sum_even_numbers(1, 10))