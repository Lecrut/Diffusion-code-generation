def count_elements(sequence):
    return sum(1 for _ in sequence)
if __name__ == '__main__':
    data = [10, 20, 30, 40]
    result = count_elements(data)
    print(result)