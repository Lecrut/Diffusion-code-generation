if __name__ == '__main__':
    input_data = "10.5 2.3 -4.8 9.1"
    numbers = [float(x) for x in input_data.split()]
    total_sum = sum(numbers)
    print(f"{total_sum:.2f}")