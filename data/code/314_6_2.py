if __name__ == '__main__':
    input_data = "10.5 2.3 4.11 0.9"
    numbers = [float(x) for x in input_data.split()]
    total_sum = sum(numbers)
    print(f"{total_sum:.2f}")