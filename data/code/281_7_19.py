def sum_ten_numbers(**kwargs):
    total = 0
    for key in kwargs:
        if not isinstance(kwargs[key], (int, float)):
            raise ValueError("All arguments must be numbers")
        total += kwargs[key]
    return total

if __name__ == '__main__':
    result = sum_ten_numbers(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10)
    print(result)