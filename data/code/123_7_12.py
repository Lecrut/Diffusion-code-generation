SUM_START = 1
SUM_END = 10

def sum_even_numbers(start=SUM_START, end=SUM_END):
    return sum(x for x in range(start, end + 1) if x % 2 == 0)

if __name__ == '__main__':
    print(sum_even_numbers())