MAX_NUMBER = 50
SKIP_EVEN = True

def process_numbers(numbers):
    for number in numbers:
        if number > MAX_NUMBER:
            break
        if SKIP_EVEN and number % 2 == 0:
            continue
        print(number)

if __name__ == '__main__':
    sample_numbers = [3, 5, 8, 10, 23, 45, 60, 70]
    process_numbers(sample_numbers)