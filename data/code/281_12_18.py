def calculate_sum(a, b, c, d, e):
    return a + b + c + d + e

if __name__ == '__main__':
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    try:
        total_sum = calculate_sum(*numbers)
        print(total_sum)
    except TypeError as e:
        print(f"Invalid input: {e}")