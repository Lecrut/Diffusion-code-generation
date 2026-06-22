def sum_numbers(**kwargs):
    total = 0
    for number in kwargs.values():
        total += number
    return total

if __name__ == '__main__':
    result = sum_numbers(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)
    print(result)