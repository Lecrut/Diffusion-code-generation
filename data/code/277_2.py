if __name__ == '__main__':
    input_data = [10, -5, 20, 0, 3, -1, 40, 0]
    sentinel = 0
    positive_count = 0
    for number in input_data:
        if number == sentinel:
            break
        if number > 0:
            positive_count += 1
        else:
            print(f"Warning: Non-positive number {number} encountered. Continuing...")
    print(f"Total positive integers entered: {positive_count}")