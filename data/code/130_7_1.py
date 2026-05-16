def process_numbers(sample_inputs):
    for number in sample_inputs:
        try:
            if number == 0:
                print(f"Input {number} is zero.")
            else:
                print(f"Input {number} is not zero.")
        except TypeError:
            print(f"Error: Input {number} is not an integer.")
if __name__ == '__main__':
    sample_inputs = [5, 0, -3, 0, 10, "a", 7.5]
    process_numbers(sample_inputs)