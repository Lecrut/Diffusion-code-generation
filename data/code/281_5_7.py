NUMBERS = (10, 20, 30, 40, 50, 60, 70, 80)

def sum_of_eight(numbers=NUMBERS):
    return sum(numbers)

if __name__ == '__main__':
    total_sum = sum_of_eight()
    print(total_sum)