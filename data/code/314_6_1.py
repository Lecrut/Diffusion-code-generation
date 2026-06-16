if __name__ == '__main__':
    input_data = "10.5 20.75 3.14 4.0"
    numbers = [float(x) for x in input_data.split()]
    total_sum = sum(numbers)
    print(f"{total_sum:.2f}")