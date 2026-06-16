if __name__ == '__main__':
    input_data = [10, 5, 20, 3]
    running_total = 0
    for item in input_data:
        if not isinstance(item, int):
            raise TypeError("All inputs must be integers.")
        running_total += item
    print(f"The running total sum is: {running_total}")