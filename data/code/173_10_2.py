def group_even_odd(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd
if __name__ == '__main__':
    unsorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [num for num in unsorted_numbers if num % 2 == 0]
    odd_numbers = [num for num in unsorted_numbers if num % 2 != 0]
    print(f"Original list: {unsorted_numbers}")
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")