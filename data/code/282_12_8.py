def calculate_total(sequence):
    return sum(x for x in sequence)

if __name__ == '__main__':
    sample_sequence = [1.2, 3.4, 5.6, 7.8]
    result = calculate_total(sample_sequence)
    print(f"The total for {sample_sequence} is: {result}")