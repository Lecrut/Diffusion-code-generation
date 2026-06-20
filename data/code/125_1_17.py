def perform_operations(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, (int, float)):
            if number > 0:
                result += number
            else:
                result -= abs(number)
        else:
            raise ValueError("All elements must be numbers")
    return result

def main():
    sample_numbers = [5, -3, 2, -1]
    result = perform_operations(sample_numbers)
    print(result)

if __name__ == '__main__':
    main()