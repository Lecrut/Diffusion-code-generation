if __name__ == '__main__':
    sample_input = [10, -5, 20, 0, 3, 15, -1, 0]
    sentinel = 0
    positive_count = 0
    for number in sample_input:
        if number == sentinel:
            break
        if number > 0:
            positive_count += 1
        else:
            print(f"Warning: Non-positive number {number} encountered, continuing.")
    print(f"Total positive integers entered: {positive_count}")