def calculate_total(sequence):
    return sum(element for element in sequence)

if __name__ == '__main__':
    sample_sequence = [3.14, 2.71, 1.618]
    result = calculate_total(sample_sequence)
    print(f"The total for {sample_sequence} is: {result}")