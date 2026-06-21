def find_middle(numbers):
    n = len(numbers)
    middle_index = n // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_input = "10.5 20.3 30.7 40.2 50.8"
    try:
        numbers = list(map(float, sample_input.split()))
        middle_value = find_middle(numbers)
        print(middle_value)
    except ValueError:
        print("Error: Input contains non-float values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")