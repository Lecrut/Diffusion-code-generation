def check_input(number):
    if number == 0:
        print("Input is zero.")
    else:
        print("Input is not zero.")
sample_values = [1, 0, -5, 100, 0, 3.14, "hello"]
for value in sample_values:
    if isinstance(value, int):
        check_input(value)
    else:
        print(f"Skipping non-integer input: {value}")
if __name__ == '__main__':
    pass