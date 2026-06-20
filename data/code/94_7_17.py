def check_any_true(boolean_list):
    return any(boolean_list)

if __name__ == '__main__':
    sample_list = [False, False, False, True, False]
    result = check_any_true(sample_list)
    print(f"Sample List: {sample_list}, Result: {result}")