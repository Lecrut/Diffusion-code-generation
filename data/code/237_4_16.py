def validate_count(count):
    if count < 1:
        raise ValueError("Count must be at least 1")
    return count

def triangular_numbers(count=12):
    count = validate_count(count)
    return [n * (n + 1) // 2 for n in range(1, count + 1)]

if __name__ == '__main__':
    print(triangular_numbers())