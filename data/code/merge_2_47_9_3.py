def calculate_product(a: int, b: int) -> None:
    try:
        product = a * b
        print(f"The product of {a} and {b} is {product}")
    except TypeError as e:
        print("Error:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))
if __name__ == '__main__':
    calculate_product(4, 5)