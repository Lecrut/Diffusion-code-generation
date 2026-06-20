MAX_NUMBER = 1000

def calculate_total_sum():
    return (MAX_NUMBER * (MAX_NUMBER + 1)) // 2

if __name__ == '__main__':
    result = calculate_total_sum()
    print(result)