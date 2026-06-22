def sum_of_twelve_numbers():
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    return sum(numbers)

if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    total_sum = sum_of_twelve_numbers()
    print(f"Sample Set: {sample_set}")
    print(f"Sum of Twelve Numbers: {total_sum}")