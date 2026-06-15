import sys
def calculate_product(numbers):
    product = 1
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("List contains non-numeric elements")
        product *= num
    return product
if __name__ == '__main__':
    input_data = [2, 3, 5, 10]
    try:
        result = calculate_product(input_data)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")