if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum_even = sum(n for n in numbers if n % 2 == 0)
    print(sum_even)