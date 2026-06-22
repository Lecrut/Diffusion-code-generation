def calculate_sum(a, b, c, d, e):
    total = a + b + c + d + e
    return total

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    computed_sum = calculate_sum(*sample_numbers)
    print(computed_sum)