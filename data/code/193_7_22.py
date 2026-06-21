def compute_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    data = [12, 34, 56, 78, 90]
    result = compute_total(data)
    print(result)