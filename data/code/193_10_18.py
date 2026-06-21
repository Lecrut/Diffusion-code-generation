TOTAL = 0

def calculate_sum(numbers):
    global TOTAL
    TOTAL += sum(numbers)

if __name__ == '__main__':
    sample_list = [1, 5, 10, -3, 8]
    calculate_sum(sample_list)
    print(TOTAL)