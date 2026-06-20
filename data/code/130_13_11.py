def is_zero(number):
    if number == 0:
        return True
    return False

if __name__ == '__main__':
    sample_values = [1, 0, -1, 5, 0.0]
    for value in sample_values:
        print(f"Is {value} zero? {is_zero(value)}")