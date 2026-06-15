if __name__ == '__main__':
    sample_numbers = [10, 25, 40, 55, 12]
    total_sum = 0
    for number in sample_numbers:
        if isinstance(number, (int, float)):
            total_sum += number
        else:
            print(f"Skipping invalid input: {number}")
    print(f"The total sum of the numbers is: {total_sum}")