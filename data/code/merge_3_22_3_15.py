# Check if an integer is odd using a single expression: num % 2 != 0
def check_odd(num):
    return num % 2 != 0

if __name__ == '__main__':
    sample_num = 17
    result = check_odd(sample_num)
    print(f"Is {sample_num} odd? {result}")