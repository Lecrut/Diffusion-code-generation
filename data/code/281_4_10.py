def sum_of_seven_integers(int_list):
    return sum(int_list)

if __name__ == '__main__':
    numbers = [4, 8, 15, 16, 23, 42, 7]
    result = sum_of_seven_integers(numbers)
    print(f"Sum of {numbers}: {result}")