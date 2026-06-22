def sum_ten_numbers(**kwargs):
    total = 0.0
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            total += value
    return total

if __name__ == '__main__':
    result = sum_ten_numbers(a=1.5, b=2.75, c=3.0, d=-4.2, e=10.1, f=6.0, g=7.5, h=8.2, i=9.0, j=10.0)
    print(result)