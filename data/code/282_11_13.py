def calculate_total(numbers):
    try:
        return sum(numbers)
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_values = (15, 25, 35, 45, 55)
    result = calculate_total(sample_values)
    print(result)