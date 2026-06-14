if __name__ == '__main__':
    limit = 1000
    total_sum = 0
    current_number = 1
    while current_number <= limit:
        total_sum += current_number
        current_number += 1
    print(f"The sum of integers from 1 to {limit} is: {total_sum}")