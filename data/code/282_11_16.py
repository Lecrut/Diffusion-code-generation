def calculate_total(numbers):
    try:
        return sum(numbers)
    except TypeError as e:
        return f"Error: {e}"

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4, 5)
    print(calculate_total(sample_values))