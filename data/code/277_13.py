def count_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count
if __name__ == '__main__':
    result = count_even_numbers()
    print(result)