def calculate_sum(a, b, c, d, e):
    total = a + b + c + d + e
    return total

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5, 5.5]
    result = calculate_sum(*sample_values)
    print(result)