def calculate_total(sequence):
    return sum(element for element in sequence)

if __name__ == '__main__':
    sample_sequence = [1.5, 2.3, 3.7, 4.1]
    result = calculate_total(sample_sequence)
    print(f"The total for {sample_sequence} is: {result}")