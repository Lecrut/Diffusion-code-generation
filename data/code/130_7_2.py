def process_numbers(sample_inputs):
    for number in sample_inputs:
        try:
            if number == 0:
                print(f"Input {number} is zero.")
            else:
                print(f"Input {number} is not zero.")
        except TypeError:
            print(f"Error: Invalid input type encountered for value {number}. Please re-enter.")
if __name__ == '__main__':
    sample_data = [5, 0, -3, 0, 10, "a", 7.5]
    process_numbers(sample_data)