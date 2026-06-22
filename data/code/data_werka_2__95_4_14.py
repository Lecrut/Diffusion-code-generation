def has_three_positive_even_divisible_by_two(numbers):
    count = 0
    for n in numbers:
        if n > 0 and n % 2 == 0:
            count += 1
            if count >= 3:
                return True
    return False

if __name__ == '__main__':
    data1 = [2, 4, 6, 1, 3, 5]
    data2 = [1, 3, 5, 7, 9]
    data3 = [2, 4, 6, 8, 10]
    data4 = [2, 4, 1, 3]
    print(has_three_positive_even_divisible_by_two(data1))
    print(has_three_positive_even_divisible_by_two(data2))
    print(has_three_positive_even_divisible_by_two(data3))
    print(has_three_positive_even_divisible_by_two(data4))