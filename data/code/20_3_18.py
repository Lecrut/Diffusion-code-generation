def is_divisible_by_two(n):
    if n % 2 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    sample_values = [4, 7, 10, -3, 0]
    for val in sample_values:
        result = is_divisible_by_two(val)
        print(result)