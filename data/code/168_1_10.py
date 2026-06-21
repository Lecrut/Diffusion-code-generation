def categorize_numbers(numbers):
    even = []
    odd = []
    
    for number in numbers:
        try:
            num = int(number)
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        except ValueError:
            raise ValueError(f"Invalid input: {number} is not a valid integer.")
    
    return {'even': even, 'odd': odd}

if __name__ == '__main__':
    sample_numbers = ['1', '2', '3', '4', '5', '6.5', '7']
    print(categorize_numbers(sample_numbers))