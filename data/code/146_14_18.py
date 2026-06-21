class NumberProcessor:
    @staticmethod
    def divide_numbers(num1, num2):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        else:
            return result

if __name__ == '__main__':
    processor = NumberProcessor()
    result = processor.divide_numbers(10, 2)
    print(result)