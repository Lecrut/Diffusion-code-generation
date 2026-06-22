def calculate_mean(numbers):
    if not numbers:
        return None
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    if count == 0:
        return None
    return total / count

if __name__ == '__main__':
    values = [10, 20, 30, 40, 50]
    result = calculate_mean(values)
    print(result)
    
    empty_values = []
    empty_result = calculate_mean(empty_values)
    print(empty_result)