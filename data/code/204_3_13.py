def find_middle(numbers):
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return None

if __name__ == '__main__':
    sample_input = "60.5 70.3 80.9 90.4 100.2"
    try:
        input_list = [float(x.strip()) for x in sample_input.split(',')]
        middle_value = find_middle(input_list)
        print(middle_value)
    except ValueError:
        print("Error: Input contains non-float values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")