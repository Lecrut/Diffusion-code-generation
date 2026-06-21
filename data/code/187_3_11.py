MAX_FLOAT = float('-inf')

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    result = max(sample_list, default=MAX_FLOAT)
    print(f"The largest value in {sample_list} is: {result}")