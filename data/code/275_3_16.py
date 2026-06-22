def count_even_numbers(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    data = [3, 4, 5, 6, 7, 8]
    result = count_even_numbers(data)
    print(result)