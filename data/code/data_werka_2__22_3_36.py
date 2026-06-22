ODD_THRESHOLD = 1

def filter_odd_numbers(numbers):
    def is_odd(num):
        return num % 2 != 0
    
    return [num for num in numbers if is_odd(num)]

if __name__ == '__main__':
    sample_values = [15, 22, 37, 48, 59, 64, 73, 86, 91, 100]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)