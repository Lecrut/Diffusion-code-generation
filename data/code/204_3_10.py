class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_middle(self):
        n = len(self.numbers)
        middle_index = n // 2
        return self.numbers[middle_index]

if __name__ == '__main__':
    sample_input = "10.5 20.3 30.7 40.2 50.8"
    try:
        numbers = list(map(float, sample_input.split()))
        processor = NumberProcessor(numbers)
        middle_value = processor.find_middle()
        print(middle_value)
    except ValueError:
        print("Error: Input contains non-integer values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")