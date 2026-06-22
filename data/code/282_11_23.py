def calculate_total(numbers):
    try:
        total = sum(numbers)
        return total
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_numbers = (15, 25, 35, 45, 55)
    result = calculate_total(sample_numbers)
    print(result)