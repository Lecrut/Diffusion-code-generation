def check_zero(number):
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is not zero.")
if __name__ == '__main__':
    sample_values = [0, 5, -10, 0.0, "abc"]
    for value in sample_values:
        try:
            if isinstance(value, int):
                check_zero(value)
            else:
                print(f"Invalid input type encountered: {value}")
        except TypeError:
            print(f"Error processing value: {value}")