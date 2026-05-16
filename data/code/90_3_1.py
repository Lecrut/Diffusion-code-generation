if __name__ == '__main__':
    value1 = 5
    value2 = 10
    try:
        result = value1 or value2
        print(f"Value 1: {value1}")
        print(f"Value 2: {value2}")
        print(f"Result of 'or' operation: {result}")
    except TypeError as e:
        print(f"An error occurred during the operation: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")