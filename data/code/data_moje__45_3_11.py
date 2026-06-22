def get_min_value(numbers):
    return min(numbers) if numbers else None

if __name__ == '__main__':
    result = get_min_value([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    print(result)